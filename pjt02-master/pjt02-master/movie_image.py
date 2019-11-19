from decouple import config
from pprint import pprint
import requests
import csv

moviecd = []
movieimage = []

with open('movie_naver.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        moviecd.append(row['movieCd'])
        movieimage.append(row['image'])

for index, imagelink in enumerate(movieimage):
    url = imagelink
    with open(f'images/{moviecd[index]}.jpg', 'wb') as f:
        image = requests.get(url, stream=True).content
        f.write(image)

