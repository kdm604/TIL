T = int(input())

for test in range(T):
    N = int(input())
    arr = [[0 for _ in range(2)]for _ in range(N)]

    for z in range(N):
        arr[z] = list(map(int, input().split()))
    P = int(input())
    ans = []
    for z in range(P):
        x = int(input())
        ans.append(x)
    visited = [0 for _ in range(5001)]

    for i in range(N):
        for j in range(arr[i][0], arr[i][1]+1):
            visited[j] += 1


    print("#%d" % (test+1),end=" ")
    for i in range(len(ans)):
        print(visited[ans[i]],end=" ")
    print()

