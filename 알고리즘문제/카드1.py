import sys
from collections import deque
sys.stdin = open("카드1.txt")

N = int(input())

arr = deque()
ans = []
for z in range(1, N+1):
    arr.append(z)

while arr:
    x = arr.popleft()
    ans.append(x)
    if arr:
        y = arr.popleft()
        arr.append(y)

for z in range(N):
    print(ans[z], end=" ")
