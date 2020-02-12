cnt = 0
nxn = [[0 for _ in range(302)]for _ in range(302)]
nxn[1][1] = 1
for i in range(1, 2):
    for j in range(2, 301):
        if nxn[j][i] == 0:
            nxn[j][i] = j - 1 + nxn[j - 1][i]

for i in range(1, 301):
    cnt = i + 1
    for j in range(2, 301):
        nxn[i][j] = nxn[i][j - 1] + cnt
        cnt += 1

T = int(input())

for test in range(T):
    P, Q = map(int, input().split())
    index = 0
    ans = []
    for i in range(1, 301):
        if len(ans) == 4:
            break
        for j in range(1, 301):
            if len(ans) == 4:
                break
            if nxn[i][j] == P:
                ans.append(i)
                ans.append(j)
            if nxn[i][j] == Q:
                ans.append(i)
                ans.append(j)

    x = ans[0] + ans[2]
    y = ans[1] + ans[3]

    print("#%d %d" % (test+1, nxn[x][y]))


