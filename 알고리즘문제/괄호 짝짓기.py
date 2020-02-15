T = 10

for test in range(T):
    N = int(input())
    arr = list(input())
    b = 0
    tmp = ['[', ']', '(', ')', '{', '}', '<', '>']
    tmp2 = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(arr)):
        for j in range(len(tmp)):
            if arr[i] == tmp[j]:
                tmp2[j] += 1

    for i in range(0, len(tmp)-1, 2):
        if tmp2[i] != tmp2[i+1]:
            b = 1
            break

    if b == 0:
        print("#%d %d" % (test+1, 1))
    else:
        print("#%d %d" % (test + 1, 0))