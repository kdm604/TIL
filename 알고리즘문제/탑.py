import sys

N = int(input())
arr = [0] + list(map(int, input().split()))
visited = [0 for _ in range(N+1)]

for i in range(1, N+1):
    j = i-1
    while j:
        tmp = arr[i]
        if arr[j] >= tmp:
            visited[i] = j
            break
        if arr[j] == tmp:
            visited[i] = visited[j]
            break
        if tmp > arr[j]:
            j = visited[j]
    if visited[i] == 0:
        visited[i] = 0

for i in range(1, N+1):
    print(visited[i], end=" ")
