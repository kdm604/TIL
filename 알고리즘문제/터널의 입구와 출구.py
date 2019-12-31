import sys

N = int(input())
M = int(input())

arr = []
ans = 0
for z in range(N):
    a, b = map(int, input().split())
    arr.append([a, b])

tmp = M

for i in range(len(arr)):
    arr[i][0] += tmp
    tmp = arr[i][0] - arr[i][1]
    if tmp < 0:
        ans = 0
        break

    if tmp > ans:
        ans = tmp

print(ans)