from decouple import config
import requests
import csv
from pprint import pprint
import datetime

key = config('API_KEY')
moviecd_list = []
info_list = [{}]

with open('boxoffice.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    # 한줄씩 읽는다.
    for row in reader:
        moviecd_list.append(row['movieCd'])
    # print(moviecd_list)

for i in moviecd_list:
    url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'
    base_url = (f'{url}?key={key}&movieCd={int(i)}')
    result = requests.get(base_url).json()
    
    dic = {}
    dic["movieCd"] = result.get("movieInfoResult").get("movieInfo").get("movieCd")
    dic["movieNm"] = result.get("movieInfoResult").get("movieInfo").get("movieNm")
    dic["movieNmEn"] = result.get("movieInfoResult").get("movieInfo").get("movieNmEn")
    dic["movieNmOg"] = result.get("movieInfoResult").get("movieInfo").get("movieNmOg")
    dic["watchGradeNm"] = result.get("movieInfoResult").get("movieInfo").get("audits")[0].get("watchGradeNm") if result.get("movieInfoResult").get("movieInfo").get("audits") else None
    dic["openDt"] = result.get("movieInfoResult").get("movieInfo").get("openDt")
    dic["showTm"] = result.get("movieInfoResult").get("movieInfo").get("showTm")
    dic["genreNm"] = result.get("movieInfoResult").get("movieInfo").get("genres")[0].get("genreNm") if result.get("movieInfoResult").get("movieInfo").get("genres") else None
    dic["peopleNm"] = result.get("movieInfoResult").get("movieInfo").get("directors")[0].get("peopleNm") if result.get("movieInfoResult").get("movieInfo").get("directors") else None
    
    info_list.append(dic)

del info_list[0]

with open('movie.csv', 'w', newline='', encoding='utf-8') as f:
    #1. 저장할 데이터들의 필드이름을 미리 지정한다
    fieldnames = ['movieCd', 'movieNm', 'movieNmEn','movieNmOg','watchGradeNm','openDt','showTm','genreNm','peopleNm']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()

    for j in info_list:
        writer.writerow(j)