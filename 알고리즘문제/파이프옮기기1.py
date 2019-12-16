import sys
from collections import deque
sys.stdin = open("파이프옮기기1.txt")
# BFS를 활용해서 그전에 파이프가 어떤 이동을 했는지 매개변수로 넘겨서 다음 이동할 수 있는 경우를 파악
# 벽이 생길 수 있으니 이동을 할때 벽(1)이 있으면 이동불가. 대각선이동을 할 때 바로옆,바로밑 좌표가 1일때 이동불가

#세로 가로 대각선으로 파이프 이동
dx = [1, 0, 1]
dy = [0, 1, 1]

direction = [[0, 1], [1, 2], [0, 1, 2]]

def bfs(x, y, dir):
    global ans
    Q = deque()
    Q.append((x, y, dir))

    while Q:
        x, y, dir = Q.popleft()
        if x == N and y == N:
            ans += 1
            continue

        for d in range(3):
            if d + dir == 1:
                continue
            nx = x + dx[d]
            ny = y + dy[d]
            if nx > N or ny > N or nxn[nx][ny]:
                continue
            if d == 2 and (nxn[x][y+1] or nxn[x+1][y]):
                continue
            Q.append((nx, ny, d))

N = int(input())
ans = 0
nxn = [[0 for _ in range(N)] for _ in range(N+1)]

for z in range(1, N+1):
    nxn[z] = [0] + list(map(int, input().split()))

if nxn[N][N] != 1:
    bfs(1, 2, 1)

print(ans)
