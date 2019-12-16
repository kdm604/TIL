import sys
sys.stdin = open("수 정렬하기.txt")

N = int(input())
number = []
ans = []
for z in range(N):
    num = int(sys.stdin.readline())
    number.append(num)

number.sort()

for z in range(N):
    ans.append(str(number[z]))

print('\n'.join(ans))

