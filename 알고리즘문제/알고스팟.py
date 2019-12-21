import sys
from collections import deque


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    Q = deque()
    Q.append((x, y))

    while len(Q):
        x, y = Q.popleft()
        for d in range(4):
            if 0 <= x+dx[d] < N and 0 <= y+dy[d] < M:
                if nxm2[x][y] + nxm[x+dx[d]][y+dy[d]] < nxm2[x+dx[d]][y+dy[d]]:
                    nxm2[x + dx[d]][y + dy[d]] = nxm2[x][y] + nxm[x+dx[d]][y+dy[d]]
                    Q.append((x+dx[d], y+dy[d]))



M, N = map(int, input().split())

nxm = [[0 for _ in range(M)]for _ in range(N)]
nxm2 = [[987654321 for _ in range(M)]for _ in range(N)]
nxm2[0][0] = 0
for z in range(N):
    nxm[z] = list(input())
    nxm[z] = list(map(int, nxm[z]))

bfs(0, 0)

print(nxm2[N-1][M-1])