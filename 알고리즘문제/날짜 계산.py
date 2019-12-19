import sys
sys.stdin = open("날짜 계산.txt")

E, S, M = map(int, input().split())
arr = [15, 28, 19]
cnt = 0
while 1:
    cnt += 1
    a = cnt % arr[0]

    if a == E or E == 15 and a == 0:
        b = cnt % arr[1]
        if b == S or S == 28 and b == 0:
            c = cnt % arr[2]
            if c == M or M == 19 and c == 0:
                break



print(cnt)