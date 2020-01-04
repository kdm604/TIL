N = int(input())
arr = []
for z in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.sort()

for z in range(N):
    print(arr[z][0], arr[z][1])