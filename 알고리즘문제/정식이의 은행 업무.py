def dfs2(tmp = []):

    if len(tmp) == len(arr):
        cnt = 0
        word = ""
        for i in range(len(tmp)):
            if cnt == 2:
                break
            word += str(tmp[i])
            if arr[i] != tmp[i]:
                cnt += 1
        if cnt == 1:
            tmp2.append(word)
        return

    tmp.append('0')
    dfs2()
    tmp.pop()
    tmp.append('1')
    dfs2()
    tmp.pop()


def dfs3(tmp = []):

    if len(tmp) == len(brr):
        cnt = 0
        word = ""
        for i in range(len(tmp)):
            if cnt == 2:
                break
            word += str(tmp[i])
            if brr[i] != tmp[i]:
                cnt += 1
        if cnt == 1:
            tmp3.append(word)
        return
    tmp.append('0')
    dfs3()
    tmp.pop()
    tmp.append('1')
    dfs3()
    tmp.pop()
    tmp.append('2')
    dfs3()
    tmp.pop()

T = int(input())
for test in range(T):
    tmp2 = []
    tmp3 = []
    ans = []
    arr = list(input())
    brr = list(input())

    for i in range(len(arr)):
        if arr[i] == '0':
            arr[i] = '1'
            tmp = ''.join(arr)
            arr[i] = '0'
            ans.append(int(tmp, 2))
        if arr[i] == '1':
            arr[i] = '0'
            tmp = ''.join(arr)
            arr[i] = '1'
            ans.append(int(tmp, 2))


    for i in range(len(brr)):
        if brr[i] == '0':
            brr[i] = '1'
            tmp = ''.join(brr)
            brr[i] = '0'
            ans.append(int(tmp, 3))
            brr[i] = '2'
            tmp = ''.join(brr)
            brr[i] = '0'
            ans.append(int(tmp, 3))

        if brr[i] == '1':
            brr[i] = '0'
            tmp = ''.join(brr)
            brr[i] = '1'
            ans.append(int(tmp, 3))
            brr[i] = '2'
            tmp = ''.join(brr)
            brr[i] = '1'
            ans.append(int(tmp, 3))

        if brr[i] == '2':
            brr[i] = '0'
            tmp = ''.join(brr)
            brr[i] = '2'
            ans.append(int(tmp, 3))
            brr[i] = '1'
            tmp = ''.join(brr)
            brr[i] = '2'
            ans.append(int(tmp, 3))

    ans.sort()

    for i in range(len(ans)):
        if ans[i] == ans[i+1]:
            break

    print("#%d %d" % (test+1, ans[i]))