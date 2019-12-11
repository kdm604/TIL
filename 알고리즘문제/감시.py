import sys
from collections import deque

# 지금 가지고있는 좌표의 값과 인구이동을 할때의 값이 달라진다면 인구이동.


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def move(x, y, s, cnt):
    global flag
    br = 0
    Q = deque()
    Q.append((x, y, s, cnt))
    visited[x][y] = count

    while len(Q):
        x, y, s, cnt = Q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if L <= abs(nxn[x][y] - nxn[nx][ny]) <= R and visited[nx][ny] != count and visited[nx][ny] != -1:
                    visited[nx][ny] = -1
                    br = 1
                    Q.append((nx, ny, s + nxn[nx][ny], cnt + 1))

    if br == 1:
        avg = s // cnt
        for i in range(N):
            for j in range(N):
                if visited[i][j] == count or visited[i][j] == -1:
                    if nxn[i][j] != avg:
                        flag = 1
                    nxn[i][j] = avg
                    visited[i][j] = 0


N, L, R = map(int, input().split())

nxn = [list(map(int, input().split())) for _ in range(N)]
count = 0
ans = [0]
flag = 1
while flag == 1:
    flag = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if visited[x][y] == 0:
                count += 1
                move(x, y, nxn[x][y], 1)

    if flag == 1:
        ans[0] += 1

print(ans[0])