import sys
sys.stdin = open("수 정렬하기.txt")

N = int(input())
number = []

for z in range(N):
    num = int(input())
    number.append(num)

number.sort()

for z in range(N):
    print(number[z])

