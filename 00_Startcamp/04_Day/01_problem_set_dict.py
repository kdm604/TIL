# """
# python dictionary 문제
# """

# #1. 평균을 구하세요

# score = {
#     '수학':80,
#     '국어':90,
#     '음악':100
# }
# sum = 0
# count = 0
# for i in score.values():
#     sum = sum + i
#     count = count+1
# print(sum/count)

# #2. 반 평균을 구하세요. -> 전체 평균
# scores = {
#     'a':{
#         '수학':80,
#         '국어':90,
#         '음악':100
#     },
#     'b':{
#         '수학':80,
#         '국어':90,
#         '음악':100
#     }
# }

# # suma = 0
# # sumb = 0
# # count1 = 0
# # count2 = 0
# # for i in scores['a'].values():
# #     suma = suma + i
# #     count1 = count1 +1
# # for i in scores['b'].values():
# #     sumb = sumb + i
# #     count2 = count2 +1
# # suma = suma/count1
# # sumb = sumb/count2

# # print((suma+sumb)/2)

# sum = 0
# count = 0
# for i in scores.values():
#     for j in scores.values():
#         sum += j
#         count += 1
# avg = sum / count
# print(avg)

#3. 도시별 최근 3일 온도입니다.

city = {
    '서울':[-6, -10, 5],
    '대전':[-3, -5, 2],
    '광주':[0, -2, 10],
    '부산':[2, -2, 9]
}

#3-1 도시별 최근 3일의 온도 평균은 ?
# for name, temp in city.items():
#     average_temp = sum(temp) / len(temp)
#     print(f'{name} : {average_temp}')
#*** 3-2 도시 중 최근 3일중에 가장 추웠던,더웠던 곳은? ***

hotcity = []
coldcity = []
min = 1000
max = -1000

for name, temp in city.items():
    for i in range(len(temp)):
        if(temp[i] < min ):
            min = temp[i]
            coldcity = name
        if(temp[i] > max):
            max = temp[i]
            hotcity = name
print(f'도시 중 최근 3일중에 가장 추웠던 곳은 {coldcity}, 가장 더웠던 곳은 {hotcity} 입니다')


#3-3 서울은 영상 2도였던 적이 있나요 ? ex. 네 있어요! or 없어요!
if(2 in city['서울']):
    print("네 있어요!")
else:
    print("없어요")



