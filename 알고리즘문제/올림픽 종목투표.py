T = int(input())

for test in range(T):
    N, M = map(int, input().split())
    arrA = list(map(int, input().split()))
    arrB = list(map(int, input().split()))
    ans = [0 for _ in range(N)]

    for i in range(len(arrB)):
        tmp = arrB[i]
        for j in range(len(arrA)):
            if arrA[j] <= tmp:
                ans[j] += 1
                break

    x = ans.index(max(ans))
    print("#%d %d" % (test+1, x+1))