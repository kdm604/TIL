def bfs(x):
    visited[x] = cnt
    Q.append(x)

    while len(Q) != 0:
        x = Q.pop(0)

        for y in range(1, 101):
            if nxn[x][y] == 1 and visited[y] == 0:
                Q.append(y)
                visited[y] = visited[x] + 1
T = 10
for test in range(T):
    Q = []
    N, S = map(int, input().split())
    nxn = [[0 for _ in range(101)]for _ in range(101)]
    visited = [0 for _ in range(101)]
    cnt = 1
    ans = 0
    maxv = 0
    arr = list(map(int, input().split()))

    for i in range(0, len(arr), 2):
        nxn[arr[i]][arr[i+1]] = 1

    bfs(S)
    maxv = max(visited)
    for i in range(100, 0, -1):
        if visited[i] == maxv:
            break


    print("#%d %d" % (test+1, i))

