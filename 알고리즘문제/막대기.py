import sys
sys.stdin = open("막대기.txt")

def dfs(x, sum, cnt):
    global ans
    if sum > N:
        return
    if sum == N:
        ans = cnt
    for i in range(x+1, len(arr)):
        dfs(i, sum+arr[i], cnt+1)


arr = [64, 32, 16, 8, 4, 2, 1]
ans = 0
N = int(input())

for i in range(len(arr)):
    dfs(i, arr[i], 1)

print(ans)