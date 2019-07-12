lunch = {
    '양자강':'054-111-1111',
    '김밥카페': '054-222-2222',
    '순남시레기':'054-333-3333'
}


#1. 방법 1

with open('lunch.csv','w',encoding='utf-8') as f:
    for item in lunch.items():
        f.write(f'{item[0]},{item[1]}\n')

