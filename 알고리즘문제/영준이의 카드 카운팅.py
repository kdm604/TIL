T = int(input())

for test in range(T):
    S = [0 for _ in range(14)]
    D = [0 for _ in range(14)]
    H = [0 for _ in range(14)]
    C = [0 for _ in range(14)]
    new = ""
    arr = list(input())
    b = 0

    for i in range(0, len(arr),3):
        new = ""
        if arr[i] == 'S':
            new += arr[i+1]
            new += arr[i+2]
            S[int(new)] += 1
        if arr[i] == 'D':
            new += arr[i+1]
            new += arr[i+2]
            D[int(new)] += 1
        if arr[i] == 'H':
            new += arr[i+1]
            new += arr[i+2]
            H[int(new)] += 1
        if arr[i] == 'C':
            new += arr[i+1]
            new += arr[i+2]
            C[int(new)] += 1

    for i in range(1, 14):
        if S[i] >= 2:
            b = 1
            break
        if D[i] >= 2:
            b = 1
            break
        if H[i] >= 2:
            b = 1
            break
        if C[i] >= 2:
            b = 1
            break

    if b == 0:
        s = S.count(1)
        d = D.count(1)
        h = H.count(1)
        c = C.count(1)

        print("#%d %d %d %d %d" % (test+1, 13-s, 13-d, 13-h, 13-c))
    else:
        print("#%d ERROR" % (test+1))