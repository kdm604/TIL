dx = [1, -1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

def check(x, y, color):

    for d in range(8):
        for k in range(1, N):
            if 0 <= x + dx[d]*k <= N and 0 <= y + dy[d]*k <= N:
                if nxn[x + dx[d]*k][y + dy[d]*k] == 0:
                    break
                if nxn[x + dx[d] * k][y + dy[d] * k] == color:
                    for p in range(1, k):
                        nxn[x + dx[d] * p][y + dy[d] * p] = color
                    break


T = int(input())
for test in range(T):
    N, M = map(int, input().split())
    nxn = [[0 for _ in range(N+1)] for _ in range(N+1)]
    cnt = 0
    cnt2 = 0
    if N == 4:
        nxn[2][2] = 2
        nxn[2][3] = 1
        nxn[3][2] = 1
        nxn[3][3] = 2
    if N == 6:
        nxn[3][3] = 2
        nxn[3][4] = 1
        nxn[4][3] = 1
        nxn[4][4] = 2
    if N == 8:
        nxn[4][4] = 2
        nxn[4][5] = 1
        nxn[5][4] = 1
        nxn[5][5] = 2

    for z in range(M):
        x, y, color = map(int, input().split())
        nxn[x][y] = color
        check(x, y, color)

    for i in range(1, N+1):
        for j in range(1, N+1):
            if nxn[i][j] == 1:
                cnt += 1
            if nxn[i][j] == 2:
                cnt2 += 1

    print("#%d %d %d" % (test+1, cnt, cnt2))