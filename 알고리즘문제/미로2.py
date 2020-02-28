dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    visited[x][y] = 1
    Q.append(x)
    Q.append(y)

    while len(Q) != 0:
        x = Q.pop(0)
        y = Q.pop(0)

        if nxn[x][y] == 3:
            ans[0] = 1
            return

        for d in range(4):
            if nxn[x + dx[d]][y + dy[d]] != 1 and visited[x + dx[d]][y + dy[d]] == 0:
                Q.append(x + dx[d])
                Q.append(y + dy[d])
                visited[x + dx[d]][y + dy[d]] = 1

T = 10

for z in range(T):
    Q = []
    test = int(input())

    nxn = [[1 for _ in range(102)] for _ in range(102)]
    visited = [[0 for _ in range(102)] for _ in range(102)]
    ans = [0]
    for p in range(1, 101):
        nxn[p] = list(map(int, input()))


    for i in range(1, 100):
        for j in range(1, 100):
            if nxn[i][j] == 2:
                bfs(i, j)

    print("#%d %d" % (test, ans[0]))

