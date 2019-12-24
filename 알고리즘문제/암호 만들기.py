def dfs(brr = []):
    cnt = 0
    aeiou = 0
    if len(brr) == C:
        cnt = brr.count(1)
        if cnt == L:
            for i in range(len(brr)):
                if brr[i] == 1 and arr[i] in ahdma:
                    aeiou += 1
            if aeiou >= 1 and L-aeiou >= 2:
                tmp = []
                for i in range(len(brr)):
                    if brr[i] == 1:
                        tmp.append(arr[i])
                tmp.sort()
                tmp = ''.join(tmp)
                ans.append(tmp)
        return

    brr.append(1)
    dfs()
    brr.pop()
    brr.append(0)
    dfs()
    brr.pop()



ahdma = ['a', 'e', 'i', 'o','u']

L, C = map(int, input().split())
arr = list(input().split())
brr =[]
ans = []
dfs()
ans.sort()
for i in range(len(ans)):
    print(ans[i])