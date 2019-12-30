import sys
sys.stdin = open("연속합.txt")
N = int(input())

arr = list(map(int, input().split()))
ans = arr[0]

for i in range(1, N):
    if arr[i-1] + arr[i] > ans or arr[i-1] + arr[i] > 0:
        if arr[i] < arr[i-1] + arr[i]:
            arr[i] = arr[i-1] + arr[i]
    if ans < arr[i]:
        ans = arr[i]

print(ans)