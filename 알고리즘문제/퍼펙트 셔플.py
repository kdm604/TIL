T = int(input())

for test in range(T):
    N = int(input())
    arr = list(input().split())
    arr2 = []
    arr3 = []
    z = len(arr)
    x = len(arr)//2+1
    if z % 2 == 0:
        x = len(arr)//2
        for i in range(len(arr)//2):
            tmp = arr[i]
            tmp2 = arr[i+x]
            arr2.append(tmp)
            arr3.append(tmp2)
        print("#%d" % (test + 1), end=" ")
        for i in range(len(arr) // 2):
            print(arr2[i], end=" ")
            print(arr3[i], end=" ")
        print()
    elif z % 2 != 0:
        for i in range(len(arr)//2):
            tmp = arr[i]
            tmp2 = arr[i+x]
            arr2.append(tmp)
            arr3.append(tmp2)
        arr2.append(arr[x-1])
        print("#%d" % (test + 1), end=" ")
        for i in range(len(arr) // 2):
            print(arr2[i], end=" ")
            print(arr3[i], end=" ")
        print(arr2[-1], end=" ")
        print()
