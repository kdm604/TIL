def dfs(idx, n, cnt, num):
    num = int(num)

    if n == cnt:
        ans.add(num)
        return


    for i in range(idx, len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] <= arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                tmp = ''.join(arr)
                tmp = int(tmp)
                dfs(i, n, cnt+1, tmp)
                arr[i], arr[j] = arr[j], arr[i]


T = int(input())

for test in range(T):
    N, count = map(int, input().split())
    arr = list(str(N))
    ans = set()

    if count > 5:
        if count % 2 == 0:
            count = 4
        else:
            count = 5

    tmp22 = str(N)

    if len(tmp22) -1 < count:
        count = len(tmp22)-1

    dfs(0, count, 0, N)





    print("#%d %d" % (test+1, max(ans)))

