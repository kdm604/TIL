from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

dir = [
    [],
    [0, 1, 2, 3],
    [0, 2],
    [1, 3],
    [0, 1],
    [1, 2],
    [2, 3],
    [0, 3]
]

def bfs(x, y):
    Q.append((x, y))

    visited[x][y] = 1
    while len(Q) != 0:

        x, y = Q.popleft()

        for d in dir[nxm[x][y]]:
            tx = x + dx[d]
            ty = y + dy[d]
            if 1 <= tx <= N and 1 <= ty <= M and visited[tx][ty] == 0 and (d + 2) % 4 in dir[nxm[tx][ty]]:
                visited[tx][ty] = visited[x][y] + 1
                Q.append((tx, ty))


T = int(input())
for test in range(T):
    Q = deque()
    N, M, x, y, time = map(int, input().split())

    nxm = [[0 for _ in range(M + 2)] for _ in range(N + 2)]
    visited = [[0 for _ in range(M + 2)] for _ in range(N + 2)]
    ans = 0

    for z in range(1, N + 1):
        nxm[z] = [0] + list(map(int, input().split())) + [0]

    bfs(x + 1, y + 1)

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if 0 < visited[i][j] <= time:
                ans += 1
    print("#%d %d" % (test + 1, ans))