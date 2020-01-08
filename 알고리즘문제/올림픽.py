import sys
sys.stdin = open("올림픽.txt")

N, K = map(int, input().split())
arr = []
ans = 0
check = 0
for z in range(N):
    brr = list(map(int, input().split()))
    a = brr.pop(0)
    brr.append(a)
    arr.append(brr)

arr.sort(reverse=True)

for i in range(N):
    if arr[i][3] == K:
        check = i

if check != 0:
    for i in range(check-1, -1, -1):
        if arr[i][0] == arr[check][0] and arr[i][1] == arr[check][1] and arr[i][2] == arr[check][2]:
            check -= 1

print(check+1)
