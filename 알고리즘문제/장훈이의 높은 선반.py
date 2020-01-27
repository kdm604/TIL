def dfs2(arr=[]):
    tmp = 0
    if len(arr) == N:
        for i in range(N):
            tmp += arr[i] * arr2[i]
        if tmp >= B:
            ans.append(tmp)
        return
    arr.append(0)
    dfs2(arr)
    arr.pop()
    arr.append(1)
    dfs2(arr)
    arr.pop()

T = int(input())

for test in range(T):
    N, B = map(int, input().split())
    arr2 = list(map(int, input().split()))
    visited = [0 for _ in range(N)]
    ans = []
    arr2.sort()
    dfs2()


    print("#%d %d" % (test+1, min(ans) - B))
