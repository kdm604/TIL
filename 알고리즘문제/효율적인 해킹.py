from collections import deque
import sys

def bfs(x):
    Q = deque()
    Q.append(x)
    visited[x] = 1

    while Q:
        x = Q.popleft()
        for y in nxn[x]:
            if visited[y] == 0:
                cnt[0] += 1
                Q.append(y)
                visited[y] = 1


N, M = map(int, input().split())

nxn = [[] for i in range(N+1)]

ans = 0
anslist = []

for z in range(M):
    a, b = map(int, sys.stdin.readline().split())
    nxn[b].append(a)

for i in range(1, N+1):
    visited = [0 for _ in range(N + 1)]
    cnt = [0]
    bfs(i)
    if cnt[0] > ans:
        ans = cnt[0]
        anslist.clear()
        anslist.append(i)
    elif cnt[0] == ans:
        anslist.append(i)

print(' '.join(map(str, anslist)))
