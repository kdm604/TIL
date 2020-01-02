import sys

# M 이라는 금액을 만들수있는 동전의 모든 경우의 수
# DP동전의 경우 더 큰 동전이 들어갈 수 있을때 그값을 빼고 갯수를 1개 추가
# 하지만 이 문제의 경우 총 갯수가 아닌 해당 동전의 갯수로 금액리스트에 저장.


T = int(input())

for test in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    M = int(input())

    DP = [0 for _ in range(M+1)]


    for z in range(len(arr)):
        for i in range(1, M+1):
            if i < arr[z]:
                continue
            if i == arr[z]:
                DP[i] += 1
            else:
                if DP[i-arr[z]] > 0:
                    DP[i] += DP[i-arr[z]]



    print(DP[M])

