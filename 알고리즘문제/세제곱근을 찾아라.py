T = int(input())
for test in range(T):
    N = int(input())
    ans = -1
    for i in range(1,1000000+1):
        if i * i * i == N:
            ans = i
            break
        if i * i * i > N:
            break

    print("#%d %d" % (test+1, ans))