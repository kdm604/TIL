import sys

N = int(input())

ans_max = [[0 for _ in range(3)]for _ in range(2)]
ans_min = [[0 for _ in range(3)]for _ in range(2)]

for i in range(1, N+1):
    arr = list(map(int, sys.stdin.readline().split()))
    ans_max[i % 2][0] = max(ans_max[(i -1)%2][0], ans_max[(i-1) %2][1]) + arr[0]
    ans_max[i % 2][1] = max(ans_max[(i - 1) % 2][0], ans_max[(i - 1) % 2][1], ans_max[(i - 1) % 2][2]) + arr[1]
    ans_max[i % 2][2] = max(ans_max[(i - 1) % 2][1], ans_max[(i - 1) % 2][2]) + arr[2]

    ans_min[i % 2][0] = min(ans_min[(i - 1) % 2][0], ans_min[(i - 1) % 2][1]) + arr[0]
    ans_min[i % 2][1] = min(ans_min[(i - 1) % 2][0], ans_min[(i - 1) % 2][1], ans_min[(i - 1) % 2][2]) + arr[1]
    ans_min[i % 2][2] = min(ans_min[(i - 1) % 2][1], ans_min[(i - 1) % 2][2]) + arr[2]

print(max(ans_max[N%2][0], ans_max[N%2][1], ans_max[N%2][2]))
print(min(ans_min[N%2][0], ans_min[N%2][1], ans_min[N%2][2]))