def bfs(x):
    visited[x] = 1

    Q.append(x)

    while len(Q) != 0:
        x = Q.pop(0)

        if x == 99:
            ans[0] = 1
            return

        for y in range(100):
            if nxn[x][y] == 1 and visited[y] == 0:
                Q.append(y)
                visited[y] = 1


T = 10

for z in range(T):
    Q = []
    nxn = [[0 for _ in range(100)] for _ in range(100)]
    visited = [0 for _ in range(100)]
    test, N = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = [0]
    for i in range(0, len(arr)-1, 2):
        nxn[arr[i]][arr[i+1]] = 1

    bfs(0)

    print("#%d %d" % (test, ans[0]))