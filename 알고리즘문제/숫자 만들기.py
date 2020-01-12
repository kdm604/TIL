def dfs(depth, sum):
    global maxnum, minnum

    if depth == len(num)-1:
        if sum > maxnum:
            maxnum = sum
        if sum < minnum:
            minnum = sum
        return

    b = num[depth+1]
    if arr[2] > 0:
        arr[2] -= 1
        dfs(depth+1, sum * b)
        arr[2] += 1
    if arr[3] > 0:
        arr[3] -= 1
        if sum < 0:
            tmp = -((-sum) // b)
        else:
            tmp = sum // b

        dfs(depth + 1, tmp)

        arr[3] += 1
    if arr[0] > 0:
        arr[0] -= 1
        dfs(depth+1, sum + b)
        arr[0] += 1
    if arr[1] > 0:
        arr[1] -= 1
        dfs(depth+1, sum - b)
        arr[1] += 1


T = int(input())

for test in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    num = list(map(int, input().split()))


    maxnum = -987654321
    minnum = 987654321

    dfs(0, num[0])

    print("#%d %d" % (test+1, maxnum - (minnum)))