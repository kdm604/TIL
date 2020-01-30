T = int(input())

for test in range(T):
    K = int(input())
    arr = list(input())
    ans = []
    for i in range(len(arr)):
        tmp = []
        tmp = arr[-1-i::]
        tmp = ''.join(tmp)
        ans.append(tmp)
    ans.sort()

    print("#%d %s" % (test+1, ans[K-1]))