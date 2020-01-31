T = int(input())
for test in range(T):
    N, P = map(int, input().split())
    x = N // P

    arr = [x for _ in range(P)]

    if x * len(arr) < N:
        y = N - x * len(arr)
        for i in range(len(arr)):
            arr[i] += 1
            y -= 1
            if y == 0:
                break
    ans = arr[0]
    for i in range(1, len(arr)):
        ans *= arr[i]
    print("#%d %d" % (test+1, ans))