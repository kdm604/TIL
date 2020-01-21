import sys
from collections import deque
sys.stdin = open("파괴된 도시.txt")

N, M = map(int, input().split())

nxm = [[0 for _ in range(N+1)]for _ in range(N+1)]

for z in range(M):
    a, b = map(int, input().split())
    nxm[a][b] = 1
    nxm[b][a] = 1

city = int(input())
arr = list(map(int, input().split()))
destroyed = set()
ans = 0
answer = []

Q = deque()

for i in arr:
    Q.append(i)

while Q:
    x = Q.popleft()
    br = 0
    tmp = []
    for y in range(1, N+1):
        if nxm[x][y] == 1:
            tmp.append(y)
            if y not in arr:
                br = 1
                break
    if br == 0:
        ans += 1
        for i in tmp:
            destroyed.add(i)
        destroyed.add(x)
        answer.append(x)


    if len(destroyed) == len(arr):
        break


if len(destroyed) == len(arr):
    print(ans)

    for i in answer:
        print(i, end=" ")
else:
    print(-1)