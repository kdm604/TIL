import sys
sys.stdin = open("바이러스.txt")

def dfs(x):
    visited[x] = 1

    for y in range(1, N+1):
        if visited[y] == 1:
            continue
        if nxn[x][y] == 1:
            dfs(y)


N = int(input())
M = int(input())

nxn = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for z in range(M):
    a, b = map(int, input().split())
    nxn[a][b] = 1
    nxn[b][a] = 1

dfs(1)
ans = visited.count(1)


print(ans-1)