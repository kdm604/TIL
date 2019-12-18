import sys
sys.stdin = open("유턴싫어.txt")

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, dir):
    for d in range(4):
        if d == dir:
            continue
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < M:
            if
            dfs(nx, ny, d)



N, M = map(int, input().split())
nxm = [[0 for _ in range(M)]for _ in range(N)]

for z in range(N):
    nxm[z] = list(input())


for x in range(N):
    for y in range(M):
        if nxm[x][y] == '.':
            dfs(x, y, 0)