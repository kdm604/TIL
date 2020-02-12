T = int(input())

for test in range(T):
    N = int(input())
    arr = [[0 for _ in range(N+2)] for _ in range(N+2)]

    arr[1][1] = 1
    for i in range(2, N+1):
        for j in range(1, i+1):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]



    print("#%d" % (test+1))
    for i in range(1, N+2):
        for j in range(1, N+2):
            if arr[i][j] > 0:
                print(arr[i][j], end=" ")
        if i != N:
            print()