import sys
from collections import deque


# K = 0 ~ 30 , W,H = 1 ~ 200   최대 200 X 200 판

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

hdx = [-2, -2, 2, 2, -1, 1, -1, 1]
hdy = [-1, 1, -1, 1, -2, -2, 2, 2]

def bfs(x, y, cnt, move):
    global ans
    Q = deque()
    Q.append((x, y, cnt, move))


    while len(Q):
        x, y, cnt, move = Q.popleft()
        if x == H-1 and y == W-1:
            ans = move
            break

        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if 0 <= nx < H and 0 <= ny < W and nxm[nx][ny] != 1:
                if visited[cnt][nx][ny] == 0:
                    visited[cnt][nx][ny] = 1
                    Q.append((nx, ny, cnt, move+1))

        if cnt > 0:
            for d in range(8):
                nx = x + hdx[d]
                ny = y + hdy[d]
                if 0 <= nx < H and 0 <= ny < W and nxm[nx][ny] != 1:
                    if visited[cnt-1][nx][ny] == 0:
                        visited[cnt-1][nx][ny] = 1
                        Q.append((nx, ny, cnt-1, move+1))

K = int(input())

W, H = map(int, input().split())

nxm = [[0 for _ in range(W)]for _ in range(H)]
visited = [[[0 for _ in range(W)]for _ in range(H)]for _ in range(K+1)]
ans = 987654321
for z in range(H):
    nxm[z] = list(map(int, input().split()))

bfs(0, 0, K, 0)
if ans == 987654321:
    print(-1)
else:
    print(ans)