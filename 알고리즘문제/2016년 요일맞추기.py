T = int(input())

for test in range(T):
    m, d = map(int, input().split())
    day = [31,29,31,30,31,30,31,31,30,31,30,31]

    sum = 0
    ans = 0

    for i in range(m-1):
        sum += day[i]
    sum += d+3
    ans = sum % 7

    print("#%d %d" % (test+1, ans))

