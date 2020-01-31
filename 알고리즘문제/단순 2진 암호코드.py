T = int(input())
for test in range(T):
    N, M = map(int, input().split())
    num = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011',
           '0110111', '0001011']

    nxn = [[0 for _ in range(M)] for _ in range(N)]
    br = 0
    bb = 0
    for i in range(N):
        nxn[i] = list(input())


    for x in range(N):
        tmp = []
        for y in range(M-7):
            a = nxn[x][y:y+7:]
            a = ''.join(a)
            if a in num:
                for z in range(y, M, 7):
                    a = nxn[x][z:z + 7]
                    a = ''.join(a)
                    for p in range(10):
                        if a == num[p]:
                            tmp.append(p)
                            if len(tmp) >= 8:
                                bb = 1
            if bb == 1:
                break


        if len(tmp) >= 8:
            for k in range(len(tmp)-7):
                sum = 0
                sum2 = 0
                for q in range(7):
                    if q % 2 == 0:
                        sum += tmp[k+q]
                    else:
                        sum2 += tmp[k+q]

                ans = sum * 3 + sum2
                if k+7 <= len(tmp):
                    ans += tmp[k+7]

                if ans % 10 == 0:
                    br = 1
                    break
        if br == 1:
            break

    if br == 1:
        print("#%d %d" % (test+1, sum+sum2+tmp[k+7]))
    if br == 0:
        print("#%d %d" % (test + 1, 0))