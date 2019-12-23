from collections import deque

def bfs(x):
    Q.append(x)
    visited[x] = 1

    while len(Q) != 0:
        x = Q.popleft()
        if x == K:
            cnt[0] = visited[x]-1
            return
        if 0 <= x-1 and visited[x-1] == 0:
            visited[x-1] = visited[x] + 1
            Q.append(x-1)

        if x+1 <= 100000 and visited[x+1] == 0:
            visited[x+1] = visited[x] + 1
            Q.append(x + 1)
        if x*2 <= 100000 and visited[x*2] == 0:
            visited[x*2] = visited[x] + 1
            Q.append(x * 2)



N, K = map(int, input().split())
visited = [0 for _ in range(100001)]
cnt = [0]
Q = deque()

bfs(N)

print(cnt[0])