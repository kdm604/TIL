dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, cnt):
    visited[x][y] = 1

    if answer[0] < cnt:
        answer[0] = cnt

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N and nxn[x][y] > nxn[nx][ny] and visited[nx][ny] == 0:
            dfs(nx, ny, cnt+1)
            visited[nx][ny] = 0


T = int(input())

for test in range(T):
    N, K = map(int, input().split())

    nxn = [[0 for _ in range(N)]for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    ans = []
    answer = [0]
    for z in range(N):
        nxn[z] = list(map(int, input().split()))
    h = 0

    for i in range(N):
        for j in range(N):
            if nxn[i][j] > h:
                h = nxn[i][j]

    for i in range(N):
        for j in range(N):
            if nxn[i][j] == h:
                ans.append((i, j))

    for i in range(N):
        for j in range(N):
            for k in range(1, K+1):
                nxn[i][j] -= k
                for z in range(len(ans)):
                    dfs(ans[z][0], ans[z][1], 1)
                    visited[ans[z][0]][ ans[z][1]] = 0

                nxn[i][j] += k

    print("#%d %d" % (test+1, answer[0]))
