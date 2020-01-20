T = int(input())

for test in range(T):
    N = int(input())

    arr = list(map(int, input().split()))
    ans = []

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            tmp = 0
            tmp2 = ""
            cnt = 0
            tmp = arr[i] * arr[j]
            tmp2 = str(tmp)
            length = len(tmp2)
            for z in range(length-1):
                if tmp2[z] <= tmp2[z+1]:
                    cnt += 1
            if length-1 == cnt:
                ans.append(tmp)


    if len(ans) == 0:
        print("#%d %d" % (test + 1, -1))
    else:
        print("#%d %d" % (test+1, max(ans)))