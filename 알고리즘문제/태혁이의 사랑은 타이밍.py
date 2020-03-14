T = int(input())

for test in range(T):
    D, H, M = map(int, input().split())
    DtoM = [769, 1440, 1440]
    D -= 11
    ans = 0
    f = 0
    for i in range(D):
        ans += DtoM[i]

    if D > 0:
        ans += H *60 + M

    if D == 0:
        H -= 11
        if H < 0:
            f = 1

        elif H >= 0:
            ans += H * 60 + M -11

    if f == 1:
        print("#%d %d" % (test + 1, -1))
    else:
        print("#%d %d" % (test + 1, ans))