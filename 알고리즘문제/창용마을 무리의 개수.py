def dfs(x):
    visited[x] = cnt


    for z in range(1, N+1):
        if nxn[x][z] == 1 and visited[z] == 0:
            dfs(z)

T = int(input())

for test in range(T):
    N, M = map(int, input().split())
    nxn = [[0 for _ in range(N+1)] for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]
    cnt = 0
    for z in range(M):
        a, b = map(int, input().split())
        nxn[a][b] = 1
        nxn[b][a] = 1

    for x in range(1, N+1):
        if visited[x] == 0:
            cnt += 1
            dfs(x)

    print("#%d %d" % (test+1, cnt))
