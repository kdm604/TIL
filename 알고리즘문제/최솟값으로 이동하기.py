T = int(input())
for test in range(T):
    W, H, N = map(int, input().split())
    way = [[1 for _ in range(2)]for _ in range(N+1)]
    ans = 0

    for z in range(1, N+1):
        way[z] = list(map(int, input().split()))

    for i in range(1, N):
        if way[i][1] < way[i+1][1] and way[i][0] < way[i+1][0]:
            for h in range(1, 10000):
                if way[i][1] == way[i+1][1]:
                    break
                if way[i][0] == way[i+1][0]:
                    break
                way[i][1] += 1
                way[i][0] += 1
                ans += 1

        if way[i][1] > way[i + 1][1] and way[i][0] > way[i + 1][0]:
            for h in range(1, 10000):
                if way[i][1] == way[i + 1][1]:
                    break
                if way[i][0] == way[i + 1][0]:
                    break
                way[i][1] -= 1
                way[i][0] -= 1
                ans += 1

        ans += abs(way[i][0] - way[i+1][0])
        ans += abs(way[i][1] - way[i+1][1])

    print("#%d %d" % (test+1, ans))