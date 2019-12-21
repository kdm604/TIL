import sys
from collections import deque


def dfs(x):
    global cnt
    cnt += 1
    vl[x] = cnt
    for y in nl[x]:
        if vl[y] == 0:
            dfs(y)


def bfs(x):
    global cnt2
    Q = deque([x])
    cnt2 += 1
    vl[x] = cnt2
    while len(Q) != 0:
        x = Q.popleft()

        for y in nl[x]:
            if vl[y] == 0:
                cnt2 += 1
                vl[y] = cnt2
                Q.append(y)


N, M, V = map(int, sys.stdin.readline().strip().split())
nl = {i: [] for i in range(1, N+1)}
for m in range(M):
    v1, v2 = map(int, sys.stdin.readline().strip().split())
    nl[v1].append(v2)
    nl[v2].append(v1)

cnt = 0
cnt2 = 0
for i in range(1, N+1):
    nl[i].sort()
vl = [0 for _ in range(N+1)]
dfs(V)
max1 = max(vl)
for i in range(1, max1+1):
    print("%d" % vl.index(i), end=" ")
vl = [0 for _ in range(N+1)]
bfs(V)
max2 = max(vl)
print()
for i in range(1, max2+1):
    print("%d" % vl.index(i), end=" ")