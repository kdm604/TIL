import sys
sys.stdin = open("에라토스테네스의 체.txt")
N, K = map(int, input().split())

# 에라토스테네스의 체
n = N
a = [0, 0] + [1]*(n-1)
primes = []
cnt = 0
ans = 0
br = 0
for i in range(2, n+1):
    if br == 1:
        break
    if a[i]:
        primes.append(i)
        cnt += 1
        if cnt == K:
            ans = i
            br = 1
            break
    for j in range(2*i, n+1, i):
        if a[j] == 1:
            cnt += 1
        a[j] = 0

        if cnt == K:
            ans = j
            br = 1
            break

print(ans)
