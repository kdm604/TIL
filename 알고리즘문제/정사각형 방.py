from collections import deque
dx = [0, 0, 1, -1]
dy = [1 ,-1, 0, 0]

def bfs(x, y, num):
    global ans2
    cnt = 0
    Q.append((x,y))
    cnt += 1
    while len(Q) != 0:
        x, y = Q.popleft()
        visited[x][y] = 1
        if cnt > ans[0]:
            ans[0] = cnt
            ans2 = num
        if cnt == ans[0]:
            if ans2 > num:
                ans2 = num

        for d in range(4):
            if 0 <= x+dx[d] <= N-1 and 0 <= y+dy[d] <= N-1:
                if nxn[x+dx[d]][y+dy[d]] == nxn[x][y] + 1:
                    Q.append((x+dx[d], y+dy[d]))
                    cnt += 1

T = int(input())
for test in range(T):
    Q = deque()
    N = int(input())
    nxn = [[0 for _ in range(N)]for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    ans = [0]
    ans2 = 0
    for z in range(N):
        nxn[z] = list(map(int, input().split()))

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                continue
            bfs(i, j, nxn[i][j])

    print("#%d %d %d" % (test+1, ans2, ans[0]))