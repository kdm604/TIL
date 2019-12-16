import sys
sys.stdin = open("그룹 단어 체커.txt")

N = int(input())
ans = 0

for z in range(N):
    arr = list(input())
    brr = [0 for _ in range(26)]
    br = 0
    for i in range(len(arr)):
        x = ord(arr[i]) - 97
        if brr[x] > 0:
            if arr[i-1] != arr[i]:
                br = 1
                break
        brr[x] += 1

    if br == 0:
        ans += 1

print(ans)