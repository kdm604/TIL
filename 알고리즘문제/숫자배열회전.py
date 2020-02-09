T = int(input())

for test in range(T):
    N = int(input())

    arr = [[0 for _ in range(N)] for _ in range(N)]
    arr2 = [[0 for _ in range(N)] for _ in range(N)]
    arr3 = [[0 for _ in range(N)] for _ in range(N)]
    arr4 = [[0 for _ in range(N)] for _ in range(N)]
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            arr2[i][j] = arr[N-1-j][i]

    for i in range(N):
        for j in range(N):
            arr3[i][j] = arr2[N-1-j][i]

    for i in range(N):
        for j in range(N):
            arr4[i][j] = arr3[N-1-j][i]


    print("#%d" % (test+1))
    for i in range(N):
        for j in range(N):
            print(arr2[i][j],end="")

        print(end=" ")
        for j in range(N):
            print(arr3[i][j],end="")
        print(end=" ")
        for j in range(N):
            print(arr4[i][j],end="")

        print()