T = int(input())

for test in range(T):
    N = int(input())
    nxn = [[0 for _ in range(N)] for _ in range(N)]
    nxn = [list(input()) for _ in range(N)]
    ans = 0
    sum = 0

    for i in range(N//2):
        for j in range(N // 2-1-i, -1, -1):
            sum += int(nxn[i][j])
            sum += int(nxn[-1-j][i])
            sum += int(nxn[i][-1-j])
            sum += int(nxn[-1-j][-1-i])

    for i in range(N):
        for j in range(N):
            ans += int(nxn[i][j])

    ans -= sum

    print("#%d %d" % (test+1, ans))