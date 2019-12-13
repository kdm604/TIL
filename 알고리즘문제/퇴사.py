import sys
sys.stdin = open("퇴사.txt")


def dfs(day, pay):
    global ans


    if pay > ans:
        ans = pay


    for i in range(day+1, N+1):
        if visited[i] == 1:
            continue
        if i-1+arr[i][0] <= N:
            visited[i] = 1
            dfs(i-1+arr[i][0], pay+arr[i][1])
            visited[i] = 0

    return

N = int(input())
arr = [(0, 0)]
for z in range(N):
    t, p = map(int, input().split())
    arr.append((t, p))

ans = 0
for i in range(1, N+1):
    if i-1+arr[i][0] <= N:
        visited = [0 for _ in range(N + 1)]
        dfs(i-1 + arr[i][0], arr[i][1])

print(ans)