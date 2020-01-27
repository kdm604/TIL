import sys
sys.stdin = open("쉬운 계단 수.txt")

N = int(input())

num = [[0 for _ in range(10)] for _ in range(N+1)]

for i in range(1, 10):
    num[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            num[i][j] = num[i-1][j + 1]
        elif j == 9:
            num[i][j] = num[i - 1][j - 1]
        else:
            num[i][j] = num[i-1][j-1] + num[i-1][j+1]

print(sum(num[N]) % 1000000000)