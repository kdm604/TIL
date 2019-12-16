import sys
sys.stdin = open("소트인사이드.txt")

N = int(input())
arr = []
while N >= 1:
    x = N % 10
    arr.append(str(x))
    N //= 10

arr.sort(reverse=True)

print(''.join(arr))