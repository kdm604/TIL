T = int(input())

for test in range(T):
    arr = [[0 for _ in range(9)] for _ in range(9)]
    arr = [list(map(int, input().split())) for _ in range(9)]
    b = 0
    for i in range(9):
        for j in range(1):
            sum = 0
            sum2 = 0
            for k in range(9):
                sum += arr[i][j+k]
                sum2 += arr[j+k][i]
            if sum != 45:
                b = 1
                break
            if sum2 != 45:
                b = 1
                break
        if b == 1:
            break


    for i in range(0,9,3):
        for j in range(0,9,3):
            sum3 = 0
            for x in range(3):
                for y in range(3):
                    sum3 += arr[i+x][j+y]

            if sum3 != 45:
                b = 1
                break
        if b == 1:
            break

    if b == 1:
        print("#%d %d" % (test+1, 0))

    if b == 0:
        print("#%d %d" % (test + 1, 1))



