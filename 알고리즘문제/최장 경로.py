def dfs(x, cnt):
    visited[x] = 1

    if ans[0] < cnt:
        ans[0] = cnt
    for y in range(1, N+1):
        if nxn[x][y] == 1 and visited[y] == 0:
            dfs(y, cnt+1)
            visited[y] = 0




T = int(input())
for test in range(T):
    Q = []
    N, M = map(int, input().split())
    visited = [0 for _ in range(N+1)]
    ans = [0]
    nxn = [[0 for _ in range(N+1)]for _ in range(N+1)]
    for z in range(M):
        a, b = map(int, input().split())

        nxn[a][b] = 1
        nxn[b][a] = 1

    for x in range(1, N+1):
        for y in range(1, N + 1):
            if nxn[x][y] == 1 and visited[x] == 0:
                dfs(x, 1)
                visited = [0 for _ in range(N + 1)]

    if ans[0] == 0 and N > 0:
        print("#%d %d" % (test+1, 1))
    else:
        print("#%d %d" % (test + 1, ans[0]))
