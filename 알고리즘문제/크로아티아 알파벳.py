import sys
sys.stdin = open("크로아티아 알파벳.txt")

trans = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

arr = input()

n = len(arr)
check = [0 for _ in range(n)]
ans = 0

for z in range(len(trans)):
    if trans[z] in arr:
        x = len(trans[z])
        for i in range(n-(x-1)):
            if check[i] == 1:
                continue
            tmp = ''
            for j in range(x):
                tmp += arr[i+j]
            if trans[z] == tmp:
                ans += 1
                for j in range(x):
                    check[i+j] = 1

for z in range(n):
    if check[z] == 0:
        ans += 1
print(ans)

