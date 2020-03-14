T = int(input())

for test in range(T):
    N, Q = map(int, input().split())
    ans = [0 for _ in range(N+1)]
    for i in range(1, Q+1):
        arr = list(map(int, input().split()))
        for j in range(arr[0], arr[1]+1):
            ans[j] = i

    print("#%d" % (test+1), end=" ")
    for i in range(1, N+1):
        print(ans[i], end=" ")
    print()
