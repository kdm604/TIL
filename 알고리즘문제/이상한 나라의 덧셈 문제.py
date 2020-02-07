T = int(input())

for test in range(T):
    N = int(input())

    for i in range(10000):
        if N <= 9:
            break
        tmp = N
        x = tmp % 10
        tmp //= 10
        y = tmp % 10
        tmp //= 10

        xy = x + y
        tmp = str(tmp)
        tmp += str(xy)
        N = int(tmp)

    if i % 2 == 0:
        print("#%d B" % (test+1))
    else:
        print("#%d A" % (test + 1))
