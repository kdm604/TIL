import sys
sys.stdin = open("회전초밥.txt")

N, D, K, C = map(int, input().split())
arr = list(map(int, sys.stdin.readlines()))
ans = 0
for i in range(K):
    arr.append(arr[i])

for i in range(N):
    brr = arr[i: i+K]
    brr.append(C)
    brr = set(brr)
    cnt = len(brr)
    if cnt > ans:
        ans = cnt

print(ans)


