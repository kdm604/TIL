def dfs(x, sum, cnt):
    visited[x] = 1
    sum += arr[x]

    if cnt == 3:
        ans.append(sum)
        return
    for i in range(7):
        if visited[i] == 1:
            continue
        dfs(i, sum, cnt+1)
        visited[i] = 0

T = int(input())

for test in range(T):
    arr = list(map(int, input().split()))
    visited = [0 for _ in range(len(arr))]
    ans = []
    cnt = 0
    for i in range(7):
        dfs(i, 0, cnt+1)
        visited[i] = 0
    ans = list(set(ans))
    ans.sort(reverse=True)

    print("#%d %d" % (test+1, ans[4]))