T = int(input())

for test in range(T):
    N = int(input())
    nxn = [[0 for _ in range(N)] for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    ans = []
    for z in range(N):
        nxn[z] = list(map(int, input().split()))

    for x in range(N):

        for y in range(N):
            cnt = 0
            cnt2 = 0
            if nxn[x][y] > 0 and visited[x][y] == 0:
                for z in range(x, N):
                    if nxn[z][y] > 0:
                        cnt += 1
                        visited[z][y] = 1
                    else:
                        break
                for z in range(y, N):
                    if nxn[x][z] > 0:
                        cnt2 += 1
                        visited[x][z] = 1
                    else:
                        break
                ans.append((cnt*cnt2,cnt, cnt2))

            for i in range(x, x+cnt):
                for j in range(y, y+cnt2):
                    visited[i][j] = 1



    ans.sort()
    # print(ans)


    print("#%d %d" % (test+1, len(ans)), end=" ")
    for i in range(len(ans)):
        print("%d %d" % (ans[i][1], ans[i][2]), end=" ")
    print()