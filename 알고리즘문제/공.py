import sys
sys.stdin = open("공.txt")

num = [0, 1, 2, 3]

N = int(input())

for z in range(N):
    a, b = map(int, input().split())
    tmp = a
    for i in range(1, 4):
        if num[i] == a:
            num[i] = b
        elif num[i] == b:
            num[i] = tmp

print(num[1])