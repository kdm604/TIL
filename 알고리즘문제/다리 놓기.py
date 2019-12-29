import sys
sys.stdin = open("다리 놓기.txt")

arr = [[0 for _ in range(30)] for _ in range(30)]

for i in range(30):
    arr[i][i] = 1
    arr[i][0] = 1

for i in range(30):
    for j in range(i):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

T = int(input())

for z in range(T):
    N, M = map(int, input().split())
    print(arr[M][N])