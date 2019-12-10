from collections import deque
import sys
sys.stdin = open("치즈.txt")

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    global cnt2
    Q = deque()
    Q.append((x, y))

    while Q:
        x, y = Q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if nxm[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    cnt2 += 1
                    Q.append((nx, ny))

N, M = map(int, input().split())
nxm = [list(map(int, input().split()))for _ in range(N)]

visited2 = [[0 for _ in range(M)] for _ in range(N)]
ans = 0
cnt2 = 0
cnt = N*M - cnt2
depth = 0

while cnt != 0:
    visited = [[0 for _ in range(M)] for _ in range(N)]
    bfs(0, 0)
    depth += 1
    cnt = 0
    for x in range(N):
        for y in range(M):
            if nxm[x][y] == 1:
                cnt += 1
            if visited[x][y] == 0:
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < N and 0 <= ny < M:
                        if visited[nx][ny] == 1:
                            visited2[x][y] = 1
    ans = cnt
    cnt = 0
    for x in range(N):
        for y in range(M):
            if visited[x][y] == 0 and visited2[x][y] == 1:
                nxm[x][y] = 0

            if nxm[x][y] == 1:
                cnt += 1

print(depth, ans)