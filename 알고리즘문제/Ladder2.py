def dfs(x, y, cnt, index):
    visited[x][y] = 1

    if x == 100:
        ans.append((cnt, index))
        return

    if nxn[x][y-1] == 1 and visited[x][y-1] == 0:
        dfs(x, y-1, cnt+1, index)

    elif nxn[x][y+1] == 1 and visited[x][y+1] == 0:
        dfs(x, y+1, cnt+1, index)

    else:
        dfs(x+1, y, cnt+1, index)

T = 10

for z in range(T):
    test = int(input())
    ans = []
    nxn = [[0 for _ in range(102)] for _ in range(102)]
    visited = [[0 for _ in range(102)] for _ in range(102)]

    for i in range(1, 101):
        nxn[i] = [0] + list(map(int, input().split())) + [0]

    for i in range(1, 101):
        if nxn[1][i] == 1:
            dfs(1, i, 1, i)
            visited = [[0 for _ in range(102)] for _ in range(102)]

    ans.sort()
    maxx = ans[0][1]
    for i in range(1, len(ans)):
        if ans[0] == ans[i]:
            if ans[i][1] > maxx:
                maxx = ans[i][1]

    print("#%d %d" % (test, maxx -1))