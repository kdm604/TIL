T = int(input())
for test in range(T):
    N = int(input())
    x = 0
    ans = 0

    arr = list(map(int, input().split()))

    arr.sort()

    for i in range(0, len(arr)-2, 2):
        x = arr[i+2] - arr[i]
        if x > ans:
            ans = x
    if len(arr) % 2 != 0:
        x = arr[-1] - arr[-1-1]
        if x > ans:
            ans = x


    for i in range(1, len(arr)-2, 2):
        x = arr[i+2] - arr[i]
        if x > ans:
            ans = x

    if len(arr) % 2 == 0:
        x = arr[-1] - arr[-1-1]
        if x > ans:
            ans = x

    y = 0
    y = arr[0] - arr[1]
    if y > ans:
        ans = y

    print("#%d %d" % (test+1, ans))