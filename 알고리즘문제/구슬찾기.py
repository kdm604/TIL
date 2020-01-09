import sys
from collections import deque
sys.stdin = open("구슬찾기.txt")

N, M = map(int, input().split())


arr = [0]
ans = [0 for _ in range(N+1)]
ans2 = [0 for _ in range(N+1)]

answer = 0
for z in range(M):
    a, b = map(int, input().split())
    arr.append((a, b))

# 나보다 작은수가 몇개인지 찾기
for i in range(1, N+1):
    cnt = 0
    Q = deque()
    Q.append(i)
    visited = [0 for _ in range(N+1)]

    while Q:
        if cnt > N / 2:
            break
        x = Q.popleft()

        for j in range(1, M+1):
            if arr[j][0] == x and visited[arr[j][1]] == 0:
                cnt += 1
                Q.append(arr[j][1])
                visited[arr[j][1]] = 1

    ans[i] = cnt

for i in range(1, N+1):
    if ans[i] > N / 2:
        answer += 1

# 나보다 큰수가 몇개인지 찾기
for i in range(1, N + 1):
    cnt = 0
    Q = deque()
    Q.append(i)
    visited = [0 for _ in range(N + 1)]

    while Q:
        if cnt > N / 2:
            break
        x = Q.popleft()
        for j in range(1, M + 1):
            if arr[j][1] == x and visited[arr[j][0]] == 0:
                cnt += 1
                Q.append(arr[j][0])
                visited[arr[j][0]] = 1
    ans2[i] = cnt

for i in range(1, N+1):
    if ans2[i] > N / 2:
        answer += 1

print(answer)