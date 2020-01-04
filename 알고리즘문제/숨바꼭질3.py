import sys
from collections import deque


def bfs(x, cnt):
    global ans
    Q = deque()
    Q.append((x, cnt))
    br = 0

    while len(Q):
        x, cnt = Q.popleft()
        if x == K and ans > cnt:
            ans = cnt
            break

        if x*2 <= 200000 and visited[x*2] == 0:
            visited[x * 2] = 1
            Q.appendleft((x*2, cnt))

        if x+1 <= 100000 and visited[x+1] == 0:
            visited[x+1] = 1
            Q.append((x+1, cnt+1))

        if 0 <= x-1 and visited[x-1] == 0:
            visited[x - 1] = 1
            Q.append((x-1, cnt+1))




N, K = map(int, input().split())
visited = [0 for _ in range(200001)]
ans = 987654321

bfs(N, 0)

print(ans)