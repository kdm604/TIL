T = int(input())

for test in range(T):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    ans = 0
    cnt = 0
    arr.sort()

    for i in range(N, 0, -1):
        cnt += 1
        if cnt == 3:
            cnt = 0
            continue
        ans += arr[i]

    print("#%d %d" % (test + 1, ans))

    # 1 2 3 4 5 6 7 8 9