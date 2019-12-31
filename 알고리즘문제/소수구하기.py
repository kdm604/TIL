import sys
sys.stdin = open("소수구하기.txt")


M, N = map(int, input().split())

# 에라토스테네스의 체
n = N
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2, n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

for i in range(len(primes)):
    if M <= primes[i] <= N:
        print(primes[i])
