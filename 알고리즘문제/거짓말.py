import sys
from collections import deque

N, M = map(int, input().split())

person = list(map(int, input().split()))

party = [[] for _ in range(M+1)]
visited = [[] for _ in range(N+1)]
check = [0 for _ in range(N+1)]
Q = deque()
lie = [[] for _ in range(M+1)]
ans = 0

for z in range(1, M+1):
    party[z] = list(map(int, input().split()))
    for i in range(1, party[z][0]+1):
        visited[party[z][i]].append(z)

person.pop(0)

for i in person:
    Q.append(i)

while Q:
    x = Q.popleft()
    check[x] = 1
    for i in visited[x]:
        for j in range(1, party[i][0]+1):
            if check[party[i][j]] == 0:
                Q.append(party[i][j])

for i in range(1, N+1):
    if check[i] == 1:
        for j in visited[i]:
            lie[j] = 1

ans = M - lie.count(1)
print(ans)