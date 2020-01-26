dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    visited[x][y] = 1
    Q.append(x)
    Q.append(y)

    while len(Q) > 0:
        x = Q.pop(0)
        y = Q.pop(0)
        visited[x][y] += 1
        for d in range(4):
            if 1 <= x + dx[d] <= N+1 and 1 <= y + dy[d] <= N+1:
                if nxn[x + dx[d]][y + dy[d]] >= 0 and visited[x + dx[d]][y + dy[d]] < 20:
                    if nxn2[x][y] + nxn[x + dx[d]][y + dy[d]] < nxn2[x + dx[d]][y + dy[d]]:
                        nxn2[x + dx[d]][y + dy[d]] = nxn2[x][y] + nxn[x + dx[d]][y + dy[d]]
                        Q.append(x + dx[d])
                        Q.append(y + dy[d])


T = int(input())

for test in range(T):
    Q = []
    N = int(input())
    nxn = [[-1 for _ in range(N+2)]for _ in range(N+2)]
    nxn2 = [[1000000 for _ in range(N+2)] for _ in range(N+2)]
    nxn2[1][1] = 0
    visited = [[0 for _ in range(N+2)] for _ in range(N+2)]

    for z in range(1, N+1):
        nxn[z] = [-1] + list(map(int, input())) + [-1]

    bfs(1, 1)

    print("#%d %d" % (test+1, nxn2[N][N]))