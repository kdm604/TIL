import sys
sys.stdin = open("피보나치 수 2.txt")

N = int(input())

fibo = [0 for _ in range(91)]

fibo[0] = 0
fibo[1] = 1

if N != 0:
    for z in range(2, N+1):
        fibo[z] = fibo[z-2] + fibo[z-1]

print(fibo[N])