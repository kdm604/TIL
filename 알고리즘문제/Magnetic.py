def check(x, y):

    if nxn[x][y] == 1:
        cnt = 1
        for i in range(1, 100-x):
            if nxn[x + i][y] == 0 or nxn[x + i][y] == nxn[x][y]:
                cnt += 1
            else:
                break
        if cnt == 100 - x:
            nxn[x][y] = 0
    if nxn[x][y] == 2:
        cnt = 0
        for j in range(x-1, -1, -1):
            if nxn[j][y] == 0 or nxn[j][y] == nxn[x][y]:
                cnt += 1
            else:
                break
        if cnt == x:
            nxn[x][y] = 0
T = 10

for test in range(T):
    N = int(input())
    nxn = [[0 for _ in range(N)] for _ in range(N)]
    nxn = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if nxn[j][i] > 0:
                check(j, i)
    ans = 0
    for i in range(N):
        tmp = 0
        count = 0
        for j in range(N):
            if nxn[j][i] > 0:
                if tmp != nxn[j][i]:
                    count += 1
                    tmp = nxn[j][i]
                    if count == 2:
                        ans += 1
                        count = 0
                        if nxn[j][i] == 1:
                            tmp = 1
                        if nxn[j][i] == 2:
                            tmp = 2


    print("#%d %d" % (test+1, ans))
