import sys

dx = [1, -1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, -1, 1, -1, 1]


N = int(input())

nxn = [[0 for _ in range(N)]for _ in range(N)]
ans = [[0 for _ in range(N)]for _ in range(N)]

for z in range(N):
    nxn[z] = list(input())

for x in range(N):
    for y in range(N):
        if '1' <= nxn[x][y] <= '9':
            for d in range(8):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < N and 0 <= ny < N:
                    ans[nx][ny] += int(nxn[x][y])

for x in range(N):
    for y in range(N):
        if '1' <= nxn[x][y] <= '9':
            ans[x][y] = '*'
        elif 10 <= ans[x][y] < 100:
            ans[x][y] = 'M'

for i in range(N):
    ans[i] = list(map(str, ans[i]))
    print(''.join(ans[i]))