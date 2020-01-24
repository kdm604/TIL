T = int(input())
for test in range(T):
    N = int(input())
    arr = []
    for z in range(N):
        tmp = input()
        arr.append((len(tmp), tmp))


    arr = list(set(arr))

    arr.sort()

    print("#%d" % (test+1))
    for i in range(len(arr)):
        print(arr[i][1])
