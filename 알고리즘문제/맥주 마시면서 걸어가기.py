import sys
from collections import deque


def bfs(x, y, cnt):
    global ans
    visited[cnt] = 1
    Q = deque()
    Q.append((x, y, cnt))

    while len(Q):
        x, y, cnt = Q.popleft()
        if x == xy[n+1][0] and y == xy[n+1][1]:
            ans = 1

        for i in range(1,n+2):
            if 1000 >= abs(x - xy[i][0]) + abs(y - xy[i][1]) and visited[i] == 0:
                visited[i] = 1
                Q.append((xy[i][0], xy[i][1], i))


T = int(input())
for test in range(T):
    xy = []
    ans = 0
    n = int(input())
    for i in range(n+2):
        a, b = map(int, input().split())
        xy.append((a, b))
    visited = [0 for _ in range(n+2)]

    bfs(xy[0][0], xy[0][1], 0)

    if ans == 1:
        print('happy')
    else:
        print('sad')