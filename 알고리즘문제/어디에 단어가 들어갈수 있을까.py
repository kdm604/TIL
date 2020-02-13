T = int(input())

for test in range(T):
    N, K = map(int, input().split())

    arr = [[0 for _ in range(N)] for _ in range(N)]
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N-K+1):
            cnt = 0
            cnt2 = 0
            for x in range(K):
                if j-1 >= 0 and arr[i][j-1] == 1:
                    break
                if arr[i][j+x] == 0:
                    break
                else:
                    cnt += 1
            for x in range(K):
                if j-1 >= 0 and arr[j-1][i] == 1:
                    break
                if arr[j+x][i] == 0 :
                    break
                else:
                    cnt2 += 1

            if j+K < N and arr[i][j+K] == 0:
                if cnt == K:
                    ans += 1
            if j+K < N and arr[j+K][i] == 0:
                if cnt2 == K:
                    ans += 1
            if j+K == N:
                if cnt == K:
                    ans += 1
                if cnt2 == K:
                    ans += 1

    print("#%d %d" % (test+1, ans))
