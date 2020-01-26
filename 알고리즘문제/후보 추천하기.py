import sys
from collections import deque
sys.stdin = open("후보 추천하기.txt")

N = int(input())
student = int(input())
arr = list(map(int, input().split()))

pic = deque()
pyo = [0 for _ in range(student+1)]

for z in range(student):
    if len(pic) < N:
        if arr[z] in pic:
            pyo[arr[z]] += 1
        else:
            pic.append(arr[z])

    else:
        if arr[z] in pic:
            pyo[arr[z]] += 1
        else:
            min = 987654321
            minindex = 0
            for i in range(len(pic)):
                if min > pyo[pic[i]]:
                    min = pyo[pic[i]]
                    minindex = i

            pyo[pic[minindex]] = 0
            pic.remove(pic[minindex])
            pic.append(arr[z])

pic = list(pic)
pic.sort()

for i in range(len(pic)):
    print(pic[i], end = " ")