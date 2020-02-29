T = int(input())
for test in range(T):
    ans = [0, 0, 0]
    N = int(input())

    ans[0] = (1 + N) * N // 2
    ans[1] = (1 + N) * N - N
    ans[2] = (1 + N) * N

    print("#%d %d %d %d" % (test + 1, ans[0], ans[1], ans[2]))