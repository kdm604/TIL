import sys
sys.stdin = open("일곱난쟁이.txt")

def dfs():
    global br
    if br == 0:
        if len(brr) > 9:
            return
        if len(brr) == 9:
            if brr.count(1) == 7:
                tmp = 0
                for i in range(9):
                    if tmp > 100:
                        return
                    if brr[i] == 1:
                        tmp += arr[i]

                if tmp == 100:
                    br = 1
                    for i in range(9):
                        if brr[i] == 1:
                            ans.append(arr[i])
                return

        brr.append(0)
        dfs()
        brr.pop()

        brr.append(1)
        dfs()
        brr.pop()


br = 0
ans = []
arr = []
brr = []
for z in range(9):
    a = int(input())
    arr.append(a)
dfs()
ans.sort()

for i in range(7):
    print(ans[i])
