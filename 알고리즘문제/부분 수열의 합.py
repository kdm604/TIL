def dfs(n, k, sum):
    if sum > K:
        return

    if n == k:
        if sum == K:
            ans[0] += 1

    else:
        visited[k] = 1
        dfs(n, k +1, sum + arr[k])
        visited[k] = 0
        dfs(n, k + 1, sum)

T = int(input())

for test in range(T):
    N, K = map(int, input().split())

    arr = list(map(int, input().split()))
    visited = [0 for _ in range(len(arr))]
    ans = [0]


    dfs(N, 0, 0)

    print("#%d %d" % (test+1, ans[0]))