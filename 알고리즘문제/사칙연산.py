T = 10
for test in range(T):
    N = int(input())
    nxn = [[0 for _ in range(4)]for _ in range(N+1)]
    tmp = []
    for i in range(1, N+1):
        arr = list(input().split())

        if len(arr) == 2:
            nxn[i][3] = int(arr[1])
        else:
            nxn[i][3] = arr[1]
            nxn[i][0] = int(arr[2])
            nxn[i][1] = int(arr[3])
    for i in range(N, 0, -1):
        if nxn[i][0] == 0:
            continue
        else:
            if nxn[i][3] == '+':
                nxn[i][3] = nxn[nxn[i][0]][3] + nxn[nxn[i][1]][3]
            if nxn[i][3] == '-':
                nxn[i][3] = nxn[nxn[i][0]][3] - nxn[nxn[i][1]][3]
            if nxn[i][3] == '*':
                nxn[i][3] = nxn[nxn[i][0]][3] * nxn[nxn[i][1]][3]
            if nxn[i][3] == '/':
                nxn[i][3] = nxn[nxn[i][0]][3] // nxn[nxn[i][1]][3]


    print("#%d %d" % (test+1, nxn[1][3]))