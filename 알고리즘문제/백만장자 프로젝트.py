T = int(input())

for test in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    maxi = N-1
    sum = 0
    for i in range(N-1, -1, -1):
        if arr[i] > arr[maxi]:
            maxi = i
        else:
            sum += arr[maxi] - arr[i]
    print("#%d %d" % (test+1, sum))





