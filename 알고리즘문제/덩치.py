import sys

# 포문 돌면서 몸무게 or 키를 비교할때 몸무게가 더 크고 키가 더 크거나 같을때만 나보다 덩치큰 사람 += 1 해주기
# 포문 돌면서 몸무게 or 키를 비교할때 키가 더 크고 몸무게가 더 크거나 같을때만 나보다 덩치큰 사람 += 1 해주기

N = int(input())
arr = []

for z in range(N):
    w, h = map(int, input().split())
    arr.append((w, h))

for i in range(N):
    cnt = 1
    cnt2 = 1
    for j in range(N):
        if i == j:
            continue
        if arr[i][0] < arr[j][0]:
            if arr[i][1] < arr[j][1]:
                cnt += 1

        if arr[i][1] < arr[j][1]:
            if arr[i][0] < arr[j][0]:
                cnt2 += 1

    if cnt > cnt2:
        print(cnt2, end=' ')

    if cnt <= cnt2:
        print(cnt, end=' ')


