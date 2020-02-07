T = int(input())

for test in range(T):
    arr = list(input().split())
    index = 0
    ans = 0
    x = len(arr[1])

    while index <= len(arr[0])-1:
        cnt = 0
        for i in range(x):
            if index+i > len(arr[0])-1:
                break
            if arr[0][index+i] == arr[1][i]:
                cnt += 1
        if cnt == x:
            ans += 1
            index += x
            continue

        index += 1
        ans += 1
    print("#%d %d" % (test+1, ans))


