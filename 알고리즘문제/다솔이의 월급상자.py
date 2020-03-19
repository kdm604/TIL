T = int(input())

for test in range(T):
    N = int(input())
    sum = 0
    for i in range(N):
        a, b = map(float, input().split())
        sum += a * b

    print("#%d %f" % (test+1, sum))