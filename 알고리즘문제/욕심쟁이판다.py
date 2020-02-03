import sys
sys.stdin = open("욕심쟁이판다.txt")

def bfs(x, y, w):
    visited[x][y] = 1
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N:
            if nxn[nx][ny] > w and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
            elif nxn[nx][ny] > w:


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N = int(input())
nxn = [[0 for _ in range(N)]for _ in range(N)]
visited = [[0 for _ in range(N)]for _ in range(N)]
for z in range(N):
    nxn[z] = list(map(int, input().split()))
arr = []
for i in range(N):
    for j in range(N):
        arr.append((nxn[i][j], i, j))
arr.sort()

for i in range(N*N):
    if visited[arr[i][1]][arr[i][2]] == 0:
        bfs(arr[i][1], arr[i][2], arr[i][0])