T = int(input())

for test in range(T):
    N, M = map(int, input().split())
    NXN = [[0 for _ in range(N)] for _ in range(N)]
    NXN = [list(map(int, input().split())) for _ in range(N)]

    sum = 0
    max = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
            for x in range(M):
                for y in range(M):
                    sum += NXN[i+x][j+y]
            if sum > max:
                max = sum


    print("#%d %d" % (test+1, max))