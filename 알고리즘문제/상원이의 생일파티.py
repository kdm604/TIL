def dfs(x):
    visited[x] = 1
    for i in range(length):
        if x not in stack:
            return

    for y in range(1, N+1):
        if nxn[x][y] == 1 and visited[y] == 0:
            dfs(y)

T = int(input())

for test in range(T):
    N, M = map(int, input().split())
    nxn = [[0 for _ in range(N+1)] for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]
    ans = [0]
    stack = []
    for z in range(M):
        a, b = map(int, input().split())
        nxn[a][b] = 1
        nxn[b][a] = 1
        if a == 1:
            stack.append(b)

    length = len(stack)
    stack.append(1)
    dfs(1)
    answer = visited.count(1)

    print("#%d %d" % (test+1, answer-1))
