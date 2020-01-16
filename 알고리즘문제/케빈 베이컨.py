import sys
from collections import deque
sys.stdin = open("케빈 베이컨.txt")

def bfs(x):
    Q.append(x)

    while Q:
        x = Q.popleft()
        for y in range(1, N+1):
            if nxn[x][y] == 1 and visited[y] == 0:
                Q.append(y)
                visited[y] = visited[x] + 1


N, M = map(int, input().split())
Q = deque()
nxn = [[0 for _ in range(N+1)]for _ in range(N+1)]
ans = [0 for _ in range(N+1)]
for z in range(M):
    a, b = map(int, input().split())
    nxn[a][b] = 1
    nxn[b][a] = 1

for i in range(1, N+1):
    visited = [0 for _ in range(N+1)]
    bfs(i)
    ans[i] = sum(visited)

answer = [987654321, 0]
for i in range(1, N+1):
    if ans[i] < answer[0]:
        answer[0] = ans[i]
        answer[1] = i

print(answer[1])