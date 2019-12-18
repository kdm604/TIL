import sys
sys.stdin = open("다리만들기2.txt")

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    visited[x][y] = cnt
    for d in range(4):
        if nxn[x + dx[d]][y + dy[d]] == 1 and visited[x + dx[d]][y + dy[d]] == 0:
            dfs(x + dx[d], y + dy[d])

def find(x):
    if p[x]:
        tmp = find(p[x])
        p[x] = tmp
        return tmp
    return x

N, M = map(int, input().split())
nxn = [[0 for _ in range(M+2)]for _ in range(N+2)]
visited = [[0 for _ in range(M + 2)] for _ in range(N + 2)]
cnt = 0
ans = []
b = 0
for z in range(1, N+1):
    nxn[z] = [0] + list(map(int, input().split())) + [0]

for i in range(1, N+1):
    for j in range(1, M + 1):
        if nxn[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            dfs(i, j)

land = cnt
for k in range(1, cnt):
    count = 0
    if b == 1:
        break
    for x in range(1, N+1):
        if b == 1:
            break
        for y in range(1, M + 1):
            if visited[x][y] == k:

                cnt = 0
                for length in range(1, M+1):
                    if 1 <= y - length < M+1:
                        if visited[x][y-length] == k:
                            break
                        if visited[x][y - length] == 0:
                            cnt += 1
                        if visited[x][y - length] > 0:
                            if cnt > 1:
                                ans.append((cnt, visited[x][y - length], k))
                                count += 1
                            break
                cnt = 0
                for length in range(1, M+1):
                    if 1 <= y + length < M + 1:
                        if visited[x][y + length] == k:
                            break
                        if visited[x][y + length] == 0:
                            cnt += 1
                        if visited[x][y + length] > 0:
                            if cnt > 1:
                                ans.append((cnt, visited[x][y + length], k))
                                count += 1
                            break

                cnt = 0
                for length in range(1, N+1):
                    if 1 <= x + length < N + 1:
                        if visited[x + length][y] == k:
                            break
                        if visited[x + length][y] == 0:
                            cnt += 1
                        if visited[x + length][y] > 0:
                            if cnt > 1:
                                ans.append((cnt, visited[x + length][y], k))
                                count += 1
                            break
                cnt = 0
                for length in range(1, N+1):
                    if 1 <= x - length < N + 1:
                        if visited[x - length][y] == k:
                            break
                        if visited[x - length][y] == 0:
                            cnt += 1
                        if visited[x - length][y] > 0:
                            if cnt > 1:
                                ans.append((cnt, visited[x - length][y], k))
                                count += 1
                            break

    if count == 0:
        b = 1
        break
if b == 0:
    ans = list(set(ans))
    ans.sort()
    answer = 0

    p = [0 for _ in range(land+1)]

    check = 0
    for i in range(len(ans)):
        if check == land-1:
            break
        x = ans[i][1]
        y = ans[i][2]
        t1 = find(x)
        t2 = find(y)
        if t1 != t2:
            p[t2] = t1
            answer += ans[i][0]
            check += 1


if b == 1 or check != land -1:
    print(-1)
if b == 0 and check == land-1:
    print(answer)