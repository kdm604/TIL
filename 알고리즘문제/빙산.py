from collections import deque
import sys
sys.stdin = open("빙산.txt")

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    ans[x][y] = 1

    while Q:
        x, y = Q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if nxm[nx][ny] > 0 and ans[nx][ny] == 0:
                    ans[nx][ny] = ans[x][y] + 1
                    Q.append((nx, ny))


N, M = map(int, input().split())
ice = []
nxm = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
br = 0
cnt = 0
flag = 0

while br <= 1:
    cnt += 1
    check = 0
    visited2 = [0 for _ in range(len(ice))]
    ans = [[0 for _ in range(M)] for _ in range(N)]
    if cnt == 1:
        for x in range(N):
            for y in range(M):
                if nxm[x][y] > 0:
                    ice.append((x, y))
                    flag = 1
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < N and 0 <= ny < M:
                            if nxm[nx][ny] == 0:
                                visited[x][y] += 1

        for x in range(N):
            for y in range(M):
                if visited[x][y] > 0:
                    nxm[x][y] -= visited[x][y]
                    if nxm[x][y] < 0:
                        nxm[x][y] = 0

    if flag == 0:
        cnt = 0
        break

    if cnt > 1:
        for i in range(len(ice)):
            x = ice[i][0]
            y = ice[i][1]
            if nxm[x][y] == 0:
                continue
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < N and 0 <= ny < M:
                    if nxm[nx][ny] == 0:
                        visited2[i] += 1

        for i in range(len(ice)):
            x = ice[i][0]
            y = ice[i][1]
            if visited2[i] == 0:
                continue
            if visited2[i] > 0:
                nxm[x][y] -= visited2[i]
                if nxm[x][y] < 0:
                    nxm[x][y] = 0
                    visited2[i] = 0

    br = 0
    for i in range(len(ice)):
        x = ice[i][0]
        y = ice[i][1]
        if nxm[x][y] > 0 and ans[x][y] == 0:
            br += 1
            if br == 2:
                break
            bfs(x, y)
        if br == 2:
            break

    if br == 0:
        cnt = 0
        break


print(cnt)


