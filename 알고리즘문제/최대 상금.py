def dfs(n, cnt, num):
    num = int(num)

    if n == cnt:
        ans.append(num)
        return


    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            tmp = ''.join(arr)
            tmp = int(tmp)
            dfs(n, cnt+1, tmp)
            arr[i], arr[j] = arr[j], arr[i]




T = int(input())

for test in range(T):
    N, count = map(int, input().split())
    arr = list(str(N))
    ans = []

    if count > 5:
        if count % 2 == 0:
            count = 4
        else:
            count = 5

    dfs(count, 0, N)

    print("#%d %d" % (test+1, max(ans)))

