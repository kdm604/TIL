def dfs(x, sum):

    if sum <= ans[0]:
        return

    for i in range(N):

        if x == N:
            ans[0] = sum

        if visited[i] == 1:
            continue
        visited[i] = 1

        dfs(x+1, sum * (nxn[x][i]/100))

        visited[i] = 0

T = int(input())

for test in range(T):
    N = int(input())
    nxn = [[0 for _ in range(N)] for _ in range(N)]
    visited = [0 for _ in range(N)]
    ans = [0]
    for z in range(N):
        nxn[z] = list(map(int, input().split()))

    dfs(0, 1)
    x = ans[0] * 100

    print("#%d %.6f" % (test+1, x))