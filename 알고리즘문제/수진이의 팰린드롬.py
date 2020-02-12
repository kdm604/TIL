def dfs(brr = []):

    if len(brr) == length:
        tmp = ""
        cnt = 0
        for i in range(length):
            if brr[i] == 1:
                tmp += arr[i]
                cnt += 1
        for i in range(length):
            if brr[i] == 1:
                for j in range(cnt):
                    if brr[i+j] == 0:
                        return
                break
        ans.append(tmp)
        return

    brr.append(0)
    dfs()
    brr.pop()
    brr.append(1)
    dfs()
    brr.pop()


T = int(input())

for test in range(T):
    ans = []
    cnt = 0
    arr = list(input())
    arr.sort()
    length = len(arr)
    dfs()

    for i in range(len(ans)):
        new = ""
        if len(ans[i]) == 0:
            continue
        else:
            new = ans[i][::-1]
            if ans[i] == new:
                cnt += 1

    print("#%d %d" % (test+1, cnt))