import sys
sys.stdin = open("연산자끼워넣기.txt")

def dfs(depth, sum):
    global ansmax, ansmin
    if depth == cnt:
        if sum > ansmax:
            ansmax = int(sum)
        if sum < ansmin:
            ansmin = int(sum)
        return
    b = arr[depth + 1]
    if brr[1] > 0:
        brr[1] -= 1
        dfs(depth + 1, sum - b)
        brr[1] += 1
    if brr[3] > 0:
        brr[3] -= 1

        if sum < 0:
            tmp = -((-sum) // b)
        else:
            tmp = sum // b

        dfs(depth + 1, tmp)
        brr[3] += 1
    if brr[0] > 0:
        brr[0] -= 1
        dfs(depth + 1, sum + b)
        brr[0] += 1
    if brr[2] > 0:
        brr[2] -= 1
        dfs(depth + 1, sum * b)
        brr[2] += 1


N = int(input())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))
cnt = len(arr) - 1
ansmax = -987654321
ansmin = 987654321

a = arr[0]

dfs(0, a)

print(ansmax)
print(ansmin)