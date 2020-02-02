import sys
from collections import deque

def bfs(x, y, dir):
    global ans
    Q.append((x, y, dir))

    while Q:
        br = 0
        x, y, dir = Q.popleft()

        visited[x][y] = 1

        for d in range(1, 5):
            ndir = (dir + d) % 4
            nx = x + dx[ndir]
            ny = y + dy[ndir]
            if 0 <= nx < N and 0 <= ny < M:
                if nxm[nx][ny] == 0 and visited[nx][ny] == 0:
                    Q.append((nx, ny, ndir))
                    ans += 1
                    br = 1
                    break
        if br == 0:
            bot[0] = x + dx[(dir+2) % 4]
            bot[1] = y + dy[(dir + 2) % 4]
            bot[2] = dir



N, M = map(int, input().split())
Q = deque()
nxm = [[0 for _ in range(M)]for _ in range(N)]
visited = [[0 for _ in range(M)]for _ in range(N)]
# 방향 북, 서 남 동

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

bot = list(map(int, input().split()))
if bot[2] == 1:
    bot[2] = 3
elif bot[2] == 3:
    bot[2] = 1
for z in range(N):
    nxm[z] = list(map(int, input().split()))
ans = 1
while 1:
    if nxm[bot[0]][bot[1]] == 1:
        break
    bfs(bot[0], bot[1], bot[2])

print(ans)