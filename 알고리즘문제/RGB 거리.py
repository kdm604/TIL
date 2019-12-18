N = int(input())
nxn = [[0 for _ in range(3)]for _ in range(N+1)]
ans = [[0 for _ in range(3)]for _ in range(N+1)]
for z in range(1, N+1):
    nxn[z] = list(map(int, input().split()))

for i in range(1, N+1):
    for j in range(3):
        if j == 0:
            tmp = ans[i-1][1] + nxn[i][0]
            tmp2 = ans[i-1][2] + nxn[i][0]
            if tmp > tmp2:
                ans[i][0] = tmp2
            else:
                ans[i][0] = tmp
        if j == 1:
            tmp = ans[i-1][0] + nxn[i][1]
            tmp2 = ans[i-1][2] + nxn[i][1]
            if tmp > tmp2:
                ans[i][1] = tmp2
            else:
                ans[i][1] = tmp
        if j == 2:
            tmp = ans[i-1][0] + nxn[i][2]
            tmp2 = ans[i-1][1] + nxn[i][2]
            if tmp > tmp2:
                ans[i][2] = tmp2
            else:
                ans[i][2] = tmp

print(min(ans[N]))