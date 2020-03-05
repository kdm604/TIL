T = int(input())

for test in range(T):
    arr = list(input())
    cnt = 0
    ans = 0

    for i in range(0, len(arr)):
        if i > cnt:
            x = i - cnt
            ans += x
            cnt += int(arr[i]) + x

        else:
            cnt += int(arr[i])

    print("#%d %d" % (test+1, ans))
