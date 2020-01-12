def comb(n, r):
    if r == 0:
        tmp = ''
        tmp2 = ''
        for i in range(0, N):
            if arr[i] not in test:
                tmp += str(arr[i])+' '
            else:
                tmp2 += str(arr[i])+' '
        teams.append([list(map(int, tmp.split())), list(map(int, tmp2.split()))])
        return
    elif n < r:
        return
    else:
        test[r-1] = arr[n-1]
        comb(n-1, r-1)
        comb(n-1, r)

def check(a, b):
    global ans
    sum1 = 0
    sum2 = 0
    for i in range(k-1):
        for j in range(i+1, k):
            sum1 += nxn[a[i]][a[j]] + nxn[a[j]][a[i]]
            sum2 += nxn[b[i]][b[j]] + nxn[b[j]][b[i]]

    tmp = abs(sum1-sum2)
    if tmp < ans:
        ans = tmp


T = int(input())

for tc in range(T):
    N = int(input())
    nxn = [[0 for _ in range(N)]for _ in range(N+1)]
    arr = [i for i in range(1, N+1)]
    test = [0 for _ in range(N//2)]
    teams = []
    k = N // 2
    for z in range(1, N+1):
        nxn[z] = [0] + list(map(int, input().split()))

    comb(N, N//2)

    ans = 987654321

    for i in range(len(teams)):
        a = teams[i][0]
        b = teams[i][1]
        check(a, b)

    print("#%d %d" % (tc+1, ans))