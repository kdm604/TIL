def dfs(n, k, cal, taste):
    if cal > L:
        return
    if n == k:
        if cal < L:
            if taste > ans[0]:
                ans[0] = taste
                return

    else:
        visited[k] = 1
        dfs(n, k +1, cal + arr[k][1], taste+arr[k][0])
        visited[k] = 0
        dfs(n, k + 1, cal, taste)

T = int(input())

for test in range(T):
    N, L = map(int, input().split())
    arr = [[0 for _ in range(2)] for _ in range(N)]
    visited = [0 for _ in range(N)]
    ans = [0]
    for z in range(N):
        arr[z] = list(map(int, input().split()))

    dfs(N, 0, 0, 0)



    print("#%d %d" % (test+1, ans[0]))