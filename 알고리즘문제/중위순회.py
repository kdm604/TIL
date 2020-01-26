def preorder_traverseM(T):
    if T:
        preorder_traverseM(int(nxn[T][2]))
        print(nxn[T][1], end="")
        preorder_traverseM(int(nxn[T][3]))


T = 10

for test in range(T):
    N = int(input())
    nxn = [[0 for _ in range(4)] for _ in range(N + 1)]
    ans = []
    for i in range(1, N + 1):
        nxn[i] = list(input().split())
        if len(nxn[i]) == 2:
            nxn[i].append(0)
            nxn[i].append(0)
        if len(nxn[i]) == 3:
            nxn[i].append(0)

    # for j in range(len(nxn)):
    #     print(j, nxn[j])

    print("#%d" % (test + 1), end=" ")
    preorder_traverseM(1)
    print()