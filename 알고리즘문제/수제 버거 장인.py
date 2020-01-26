def check(n,k):
    global cnt

    for i in range(len(tmp)):
        if A[tmp[i][0]-1] == 1 and A[tmp[i][1]-1] == 1:
            return
    if n == k:
        cnt += 1

    else:
        A[k] = 1
        check(n,k+1)
        A[k] = 0
        check(n, k + 1)


T = int(input())

for test in range(T):

    N, M = map(int, input().split())
    A = [0 for _ in range(N)]
    tmp = []
    cnt = 0
    for z in range(M):
        a, b = map(int, input().split())
        tmp.append((a, b))

    check(N, 0)
    print("#%d %d" % (test+1, cnt))