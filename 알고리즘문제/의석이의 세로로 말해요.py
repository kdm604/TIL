T = int(input())

for test in range(T):

    arr = [list(input()) for _ in range(5)]
    max = 0
    length = 0
    for i in range(5):
        length = len(arr[i])
        if length > max:
            max = length


    print("#%d" % (test+1), end=" ")
    for i in range(max):
        for j in range(5):
            if len(arr[j]) <= i:
                continue

            print(arr[j][i], end="")
    print()

