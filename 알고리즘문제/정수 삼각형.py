N = int(input())

nxn = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
ans = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for z in range(1, N + 1):
    nxn[z] = [0] + list(map(int, input().split()))
    while len(nxn[z]) <= N:
        nxn[z].append(0)
ans[1][1] = nxn[1][1]

for i in range(2, N + 1):
    for j in range(1, len(nxn[i])):
        tmp = ans[i - 1][j]
        tmp2 = ans[i - 1][j - 1]

        if tmp > tmp2:
            ans[i][j] = tmp + nxn[i][j]
        else:
            ans[i][j] = tmp2 + nxn[i][j]

print(max(ans[N]))
