T = int(input())

for test in range(T):

    arr = list(map(int, input().split()))
    nxn = [[0 for _ in range(arr[0])] for _ in range(arr[0])]
    index = -1
    for i in range(1, len(arr), arr[0]):
        index += 1
        tmp = arr[i:i + arr[0]]
        nxn[index] = list(tmp)

    for i in range(arr[0]):
        for j in range(arr[0]):
            if nxn[i][j] == 0 and i != j:
                nxn[i][j] = 987654321

    for k in range(arr[0]):
        for i in range(arr[0]):
            for j in range(arr[0]):
                nxn[i][j] = min(nxn[i][k] + nxn[k][j], nxn[i][j])

    ans = min([sum(nxn[i]) for i in range(len(nxn))])

    print("#%d %d" % (test + 1, ans))