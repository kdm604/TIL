T = int(input())
for test in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    sum = {0}
    for i in arr:
        for j in list(sum):
            sum.add(j+i)
    print("#%d %d" % (test+1, len(sum)))








