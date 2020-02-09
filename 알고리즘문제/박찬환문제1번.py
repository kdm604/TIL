import sys
sys.stdin = open("박찬환문제1번.txt")
# 최소 횟수를 찾아야 하기때문에 가장 먼저 일을 할 곳 부터 찾는게 선행되어야 함.
# 가장 먼저 일할곳은 가장 처음과 끝이 될 수 있는 곳.
# 즉 1인 곳으로 들어가서 4방향 서치해서 주변에 1이 가장 적은 곳



T = int(input())

for test in range(1, T+1):
    N, M = map(int, input().split())
    nxm = [[0 for _ in range(M)]for _ in range(N)]
    for z in range(N):
        nxm[z] = list(map(int, input().split()))

    print(nxm)