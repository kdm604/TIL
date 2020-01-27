T = int(input())

for test in range(T):
    N, K = map(int, input().split())
    arr = list(input())
    ans = []
    tmp = ""
    cnt = N // 4

    for z in range(cnt):
        for i in range(0, len(arr), cnt):
            tmp = ""
            for j in range(cnt):
                tmp += arr[i + j]
            tmp = int(tmp, 16)
            ans.append(tmp)

        x = arr.pop()
        arr.insert(0, x)

    ans = list(set(ans))
    ans.sort(reverse=True)

    print("#%d %d" % (test + 1, ans[K - 1]))
