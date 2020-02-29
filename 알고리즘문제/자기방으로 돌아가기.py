T = int(input())

for test in range(T):
    N = int(input())
    nxn = [0 for _ in range(401)]
    ans = 0

    for z in range(N):
        arr = list(map(int, input().split()))
        if arr[0] % 2 == 0:
            arr[0] -= 1
        if arr[1] % 2 == 0:
            arr[1] -= 1

        if arr[0] <= arr[1]:
            for x in range(arr[0], arr[1]+1):
                nxn[x] += 1
        if arr[0] > arr[1]:
            for x in range(arr[1], arr[0]+1):
                nxn[x] += 1

    ans = max(nxn)

    print("#%d %d" % (test+1, ans))