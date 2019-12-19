import sys
sys.stdin = open("시험감독.txt")

# 총감독관1 부감독관 여러명. 이문제의 관건은 총감독관을 어디에 배치하느냐


N = int(input())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

sum = N
for i in range(N):
    arr[i] -= brr[0]

    if arr[i] <= 0:
        continue

    a = arr[i] // brr[1]
    b = arr[i] % brr[1]
    if b != 0:
        a += 1

    sum += a



print(sum)