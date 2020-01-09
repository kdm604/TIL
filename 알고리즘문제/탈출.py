import sys
from collections import deque
sys.stdin = open("탈출.txt")

def bfs():
    global ans

    while Q:
        x, y, c, a = Q.popleft()
        if a == 0:
            if nxm[x][y] == 'D':
                ans = c
                break
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < R and 0 <= ny < C and nxm[nx][ny] == '.':
                if a == 1:
                    nxm[nx][ny] = '*'
                    Q.append((nx, ny, c + 1, a))
                if a == 0 and visited[nx][ny] == 0:
                    Q.append((nx, ny, c+1, a))
                    visited[nx][ny] = 1



            if 0 <= nx < R and 0 <= ny < C and nxm[nx][ny] == 'S':
                if a == 1:
                    nxm[nx][ny] = '*'
                    Q.append((nx, ny, c+1, a))

            if 0 <= nx < R and 0 <= ny < C and nxm[nx][ny] == 'D':
                if a == 0:
                    Q.append((nx, ny, c+1, a))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
Q = deque()

R, C = map(int, input().split())
s = [0, 0]
w = []

ans = 0
nxm = [[0 for _ in range(C)]for _ in range(R)]
visited = [[0 for _ in range(C)]for _ in range(R)]
for z in range(R):
    nxm[z] = list(input())

for x in range(R):
    for y in range(C):
        if nxm[x][y] == 'S':
            s[0] = x
            s[1] = y

        if nxm[x][y] == '*':
            Q.append((x, y, 0, 1))

Q.append((s[0], s[1], 0, 0))
bfs()

if ans == 0:
    print('KAKTUS')
else:
    print(ans)