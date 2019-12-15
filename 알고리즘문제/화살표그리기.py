import sys
sys.stdin = open("화살표그리기.txt")

N = int(input())

arr = [[] for _ in range(N+1)]

crr = []
ans = 0
for z in range(N):
    crr = list(map(int, input().split()))
    arr[crr[1]].append(crr[0])


for i in range(N):
    arr[i].sort()


for j in range(N+1):
    for i in range(len(arr[j])):
        if i == 0:
            ans += abs(arr[j][0] - arr[j][1])
        elif i == len(arr[j])-1:
            ans += abs(arr[j][i] - arr[j][i-1])
        else:
            tmp = abs(arr[j][i] - arr[j][i-1])
            tmp2 = abs(arr[j][i] - arr[j][i+1])
            if tmp < tmp2:
                ans += tmp
            else:
                ans += tmp2

print(ans)



