from collections import deque
import sys

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, br, cnt):
    global answer
    Q = deque()
    Q.append((x, y, br, cnt))

    while Q:
        x, y, br, cnt = Q.popleft()
        if x == N - 1 and y == M - 1 and br <= 1:
            if answer > cnt:
                answer = cnt

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                tmp = cnt + 1

                if br == 0:
                    if nxm[nx][ny] == 0:
                        if ans[0][nx][ny] > tmp:
                            ans[0][nx][ny] = tmp
                            Q.append((nx,ny,br,cnt+1))

                    if nxm[nx][ny] == 1:
                        if ans[1][nx][ny] > tmp:
                            ans[1][nx][ny] = tmp
                            Q.append((nx, ny, br+1, cnt + 1))

                if br == 1:
                    if nxm[nx][ny] == 0:
                        if ans[1][nx][ny] > tmp:
                            ans[1][nx][ny] = tmp
                            Q.append((nx, ny, br, cnt + 1))


N, M = map(int, input().split())

nxm = [[0 for _ in range(M)] for _ in range(N)]
ans = [[[987654321 for _ in range(M)] for _ in range(N)]for _ in range(2)]

ans[0][0][0] = 0
answer = 987654321
for z in range(N):
    nxm[z] = list(map(int, input()))

bfs(0, 0, 0, 1)

if answer == 987654321:
    print(-1)
else:
    print(answer)

