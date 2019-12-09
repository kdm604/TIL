from collections import deque
import sys
sys.stdin = open("안전 영역.txt")

# 물에 잠긴 지역이 없을경우 안전 영역은 1개 덩어리
# 그래서 ans 를 0이 아닌 1로 초기화를 해둬야댐
# 높이가 1 ~ 100 까지 올수 있으므로 안전 영역이 최대가 되려면 하나 건너뛰어서 안전영역이 되어야함
# 고로 1부터 100까지 전부 물에 잠기게 하고 안전 영역의 갯수를 세면 최대 안전영역을 구할수 있음


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    visited[x][y] = cnt
    Q.append((x, y))

    while len(Q) != 0:
        x, y = Q.popleft()
        for d in range(4):
            if 1 <= x + dx[d] <= N and 1 <= y + dy[d] <= N:
                if nxn[x + dx[d]][y + dy[d]] > k and visited[x + dx[d]][y + dy[d]] == 0:
                    visited[x + dx[d]][y + dy[d]] = cnt
                    Q.append((x+dx[d], y + dy[d]))


N = int(input())
Q = deque()
nxn = [[0 for _ in range(N+2)]for _ in range(N+2)]
for z in range(1, N+1):
    nxn[z] = [0] + list(map(int, input().split())) +[0]

ans = [1]

for k in range(1, 101):
    cnt = 0
    visited = [[0 for _ in range(N + 2)] for _ in range(N + 2)]
    for i in range(1, N+1):
        for j in range(1, N + 1):
            if nxn[i][j] > k and visited[i][j] == 0:
               cnt += 1
               bfs(i, j)

    if cnt > ans[0]:
        ans[0] = cnt

print(ans[0])