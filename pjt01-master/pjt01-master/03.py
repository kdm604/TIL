from decouple import config
import requests
import csv
from pprint import pprint
import datetime

key = config('API_KEY')

P_list = []
PP_list = [{}]
with open('movie.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)

      # 한줄씩 읽는다.
    for row in reader:
        P_list.append(row['peopleNm'])

for i in P_list:
    url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json'
    base_url = (f'{url}?key={key}&peopleNm={i}')
    result = requests.get(base_url).json()

    dic = {}
    dic["peopleCd"] = result.get("peopleListResult").get("peopleList")[0].get("peopleCd") if result.get("peopleListResult").get("peopleList")[0].get("peopleCd") else None
    dic["peopleNm"] = result.get("peopleListResult").get("peopleList")[0].get("peopleNm") if result.get("peopleListResult").get("peopleList")[0].get("peopleNm") else None
    dic["repRoleNm"] = result.get("peopleListResult").get("peopleList")[0].get("peopleNm") if result.get("peopleListResult").get("peopleList")[0].get("repRoleNm") else None
    dic["filmoNames"] = result.get("peopleListResult").get("peopleList")[0].get("filmoNames") if result.get("peopleListResult").get("peopleList")[0].get("filmoNames") else None

    PP_list.append(dic)

del PP_list[0]

with open('director.csv', 'w', newline='', encoding='utf-8') as f:
    #1. 저장할 데이터들의 필드이름을 미리 지정한다
    fieldnames = ['peopleCd', 'peopleNm', 'repRoleNm','filmoNames']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()

    for j in PP_list:
        writer.writerow(j)