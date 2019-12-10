import sys
sys.stdin = open("단지번호붙이기.txt")

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    visited[x][y] = cnt

    for d in range(4):
        if 0<= x + dx[d] <= N-1 and 0 <= y + dy[d] <=N-1:
            if nxn[x+dx[d]][y+dy[d]] == '1' and visited[x+dx[d]][y+dy[d]] == 0:
                dfs(x+dx[d], y+dy[d])



N = int(input())

nxn = [[0 for _ in range(N)]for _ in range(N)]
visited = [[0 for _ in range(N)]for _ in range(N)]
ans = []
cnt = 0
cnt2 = 0
for z in range(N):
    nxn[z] = list(input())


for i in range(N):
    for j in range(N):
        if nxn[i][j] == '1' and visited[i][j] == 0:
            cnt += 1
            dfs(i, j)

for k in range(1, cnt+1):
    cnt2 = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == k:
                cnt2 += 1
    ans.append(cnt2)


ans.sort()
print(cnt)
for i in range(len(ans)):
    print(ans[i])