T = 10
for test in range(T):
    N = int(input())
    arr = list(input())
    tmp1 = []
    tmp2 = []
    for z in range(len(arr)):
        if '0' <= arr[z] <= '9':
            tmp1.append(int(arr[z]))
        else:
            if len(tmp1) >= 2:
                x = tmp1.pop()
                y = tmp1.pop()
                xy = x + y
                tmp1.append(xy)
            else:
                tmp2.append(arr[z])
    if len(tmp2) > 0:
        x = tmp1.pop()
        y = tmp1.pop()
        xy = x + y
        tmp1.append(xy)
    print("#%d %d" % (test+1, tmp1[0]))



