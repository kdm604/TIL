import sys

N, M = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = 0
br = 0
nxm = [[0 for _ in range(M)]for _ in range(N)]
for z in range(N):
    nxm[z] = list(input())
for i in range(N):
    for j in range(M):
        if nxm[i][j] == '.':
            cnt = 0
            for d in range(4):
                ni = i + dx[d]
                nj = j + dy[d]
                if 0 <= ni < N and 0 <= nj < M:
                    if nxm[ni][nj] == '.':
                        cnt += 1
            if cnt < 2:
                ans = 1
                br = 1
                break
    if br == 1:
        break
print(ans)