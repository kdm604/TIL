import sys
from collections import deque
sys.stdin = open("유기농 배추")


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    visited[x][y] = cnt

    while Q:
        x, y = Q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if nxm[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = cnt
                    Q.append((nx, ny))



T = int(input())

for test in range(T):
    M, N, K = map(int, input().split())
    nxm = [[0 for _ in range(M)]for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 0

    for z in range(K):
        y, x = map(int, input().split())
        nxm[x][y] = 1

    for x in range(N):
        for y in range(M):
            if nxm[x][y] == 1 and visited[x][y] == 0:
                cnt += 1
                bfs(x, y)

    print(cnt)

