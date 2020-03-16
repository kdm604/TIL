T = int(input())

for test in range(T):
    arr = list(input())
    H = int(input())
    order = list(map(int, input().split()))
    length = len(arr)
    ans = [0 for _ in range(length+1)]



    for i in range(H):
        ans[order[i]] += 1

    print("#%d" % (test+1), end=" ")
    for j in range(length+1):
        if ans[j] > 0:
            for k in range(ans[j]):
                print('-', end="")
        if j < length:
            print(arr[j],end="")
    print()
