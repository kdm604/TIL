import sys
from collections import deque

def bfs(x):
    Q.append((x, 0))

    while len(Q):
        x, sum = Q.popleft()
        for i in range(len(di[x])):
            if len(di[x]) > 0:
                if di[x][i][1] + sum < D[di[x][i][0]]:
                    D[di[x][i][0]] = di[x][i][1] + sum
                    Q.append((di[x][i][0], D[di[x][i][0]]))

Q = deque()
N = int(input())
M = int(input())
di = {i:[] for i in range(N+1)}
D = [987654321 for _ in range(N+1)]
for z in range(M):
    s, e, w = map(int, sys.stdin.readline().split())
    di[s].append([e, w])
S, E = map(int, input().split())


D[S] = 0
bfs(S)

print(D[E])