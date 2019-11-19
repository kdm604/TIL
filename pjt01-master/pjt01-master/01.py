from decouple import config
import requests
import csv
from pprint import pprint
import datetime

key = config('API_KEY')
targetDt = '20190713'
weekGb = '0'

movie_list=[]

date = datetime.datetime(2019, 7 ,13)

with open('boxoffice.csv', 'w', newline='', encoding='utf-8') as f:
    #1. 저장할 데이터들의 필드이름을 미리 지정한다
    fieldnames = ['movieCd', 'movieNm', 'audiAcc']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    #2. 필드 이름을 csv 파일 최상단에 작성한다.
    writer.writeheader()
    for i in range(50):
        t_time = date - datetime.timedelta(weeks=i)
        targetDt = t_time.strftime('%Y%m%d')
     
        url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
        base_url = (f'{url}?key={key}&targetDt={targetDt}&weekGb={weekGb}')
        result = requests.get(base_url).json()
        a = result.get('boxOfficeResult').get('weeklyBoxOfficeList')

    #3. dictionary를 순회하며(돈다!) key에 해당하는 value를 한줄씩 작성한다
        for newdict in result.get('boxOfficeResult').get('weeklyBoxOfficeList'):
            cnt = 0
            dic = {}
            for k,value in newdict.items():
                if k == 'movieCd':
                    if value in movie_list:
                        cnt = 1
                        break
                    else:
                        movie_list.append(value)
                if k == 'movieCd' or k == 'movieNm' or k == 'audiAcc':
                    dic.update([[k,value]])
            if cnt == 1 :
                continue
            writer.writerow(dic)
            del dic
