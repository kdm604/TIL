T = int(input())
for test in range(T):
    D, A, B, F = map(int, input().split())

    ans = float(D / (A + B))

    print("#%d %f" % (test + 1, ans * F))
