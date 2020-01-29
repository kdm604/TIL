def check(T):
    if T:
        ans.append(nxn[T][2])
        check(nxn[T][2])
def check2(T):
    if T:
        ans2.append(nxn[T][2])
        check2(nxn[T][2])
def number(T):
    if T:
        num.append(T)
        number(nxn[T][0])
        number(nxn[T][1])
T = int(input())

for test in range(T):
    V, E, A, B = map(int, input().split())
    nxn = [[0 for _ in range(3)] for _ in range(V + 1)]
    arr = list(map(int, input().split()))
    ans = []
    ans2 = []
    max = 0
    b = 0
    for i in range(0, len(arr), 2):
        if nxn[arr[i]][0] == 0:
            nxn[arr[i]][0] = arr[i + 1]
            nxn[arr[i + 1]][2] = arr[i]
        else:
            nxn[arr[i]][1] = arr[i + 1]
            nxn[arr[i + 1]][2] = arr[i]
    check(A)
    check2(B)

    for i in range(len(ans)):
        for j in range(len(ans2)):
            if ans[i] == ans2[j]:
                max = ans[i]
                b = 1
                break
        if b == 1:
            break

    num = []
    number(max)
    print("#%d %d %d" % (test+1, max, len(num)))
