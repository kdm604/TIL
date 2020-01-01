import sys

try:
    while 1:
        N, M = map(int, input().split())
        arr = []

        ans = 0
        for i in range(N, M + 1):
            arr.append(str(i))

        for i in range(len(arr)):
            br = 0
            num = [0 for _ in range(10)]

            for j in range(len(arr[i])):
                num[int(arr[i][j])] += 1

            for z in range(10):
                if num[z] > 1:
                    br = 1
                    break

            if br == 0:
                ans += 1

        print(ans)
except:
    pass