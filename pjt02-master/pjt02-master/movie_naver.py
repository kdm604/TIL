from decouple import config
from pprint import pprint
import requests
import csv



client_id = config('NAVER_CLIENT_ID')
client_secret = config('NAVER_CLIENT_SECRET')

headers = {
    'X-Naver-Client-Id': client_id, 
    'X-Naver-Client-Secret': client_secret
    }

moviecd = []
movienm = []
m_list = [{}]
with open('movie.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        moviecd.append(row['movieCd'])
        movienm.append(row['movieNm'])


for index, name in enumerate(movienm):
    movie = name
    url = f'https://openapi.naver.com/v1/search/movie.json?query={movie}'
    requests.get(url, headers=headers).json()
    response = requests.get(url, headers=headers).json()
   
    dic = {}
    if len(response.get("items")) == 1:
        a = response.get("items")[0]
    else:
        for ind, t in enumerate(response.get("items")):
            if t["title"] == f'<b>{movie}</b>':
                a = response.get("items")[ind]
                break

    dic["movieCd"] = moviecd[index]
    dic["link"] = a.get("link")
    dic["image"] = a.get("image") if a.get("image") else None
    dic["userRating"] = a.get("userRating")
    m_list.append(dic)

del m_list[0]

with open('movie_naver.csv', 'w', newline='', encoding='utf-8') as f:
    #1. 저장할 데이터들의 필드이름을 미리 지정한다
    fieldnames = ['movieCd', 'image', 'link', 'userRating']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()

    for j in m_list:
        writer.writerow(j)
