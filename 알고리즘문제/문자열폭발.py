import sys

arr = list(input())
b = list(input())
cnta = len(arr)
cntb = len(b)

brr = []
index = 0
while index < cnta:
    brr.append(arr[index])
    cntbrr = len(brr)
    check = 0

    if len(brr) >= cntb:
        for j in range(cntbrr-cntb, cntbrr):
            if brr[j] == b[check]:
                check += 1
            else:
                break
        if check == cntb:
            for j in range(cntb):
                brr.pop()

    index += 1




if len(brr) > 0:
    print(''.join(brr))
else:
    print('FRULA')
