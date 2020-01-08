import sys
sys.stdin = open("지능형기차.txt")



ans = 0
cnt = 0
for z in range(4):
    a, b = map(int, input().split())
    cnt -= a
    cnt += b

    if cnt > ans:
        ans = cnt

print(ans)
