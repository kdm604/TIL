import sys
sys.stdin = open("방 번호.txt")

# N는 1,000,000 보다 작다
N = list(input())
count = len(N)
arr = [0 for _ in range(len(N))]
br = 1
cnt = 0
while br:
    check = 0
    cnt += 1
    brr = [0 for _ in range(10)]

    for i in range(len(N)):
        if arr[i] == 1:
            continue

        for j in range(len(brr)):
            if brr[j] == 1:
                continue
            if j == 6:
                if N[i] == '9':
                    arr[i] = 1
                    brr[j] = 1
                    break

            if j == 9:
                if N[i] == '6':
                    arr[i] = 1
                    brr[j] = 1
                    break

            if N[i] == str(j):
                arr[i] = 1
                brr[j] = 1
                break

    for z in range(len(N)):
        if arr[z] == 1:
            check += 1

    if check == count:
        br = 0

print(cnt)