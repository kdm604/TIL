import sys
sys.stdin = open("치킨배달.txt")

def check(z):
    cnt = 0
    for i in range(len(house)):
        tmp = []
        x = house[i][0]
        y = house[i][1]
        for j in range(len(ans[z])):
            cx = ans[z][j][0]
            cy = ans[z][j][1]
            xy = abs(x-cx) + abs(y-cy)
            tmp.append(xy)
        tmp.sort()
        cnt += tmp[0]

    if cnt < answer[0]:
        answer[0] = cnt
    return

def dfs(brr = []):
    cnt = 0
    if len(brr) == len(chicken):
        cnt = brr.count(1)
        if cnt == M:
            tmp = []
            for i in range(len(brr)):
                if brr[i] == 1:
                    tmp.append(chicken[i])
            ans.append(tmp)
        return

    brr.append(1)
    dfs()
    brr.pop()
    brr.append(0)
    dfs()
    brr.pop()

N, M = map(int, input().split())

nxn = [[0 for _ in range(N+1)]for _ in range(N+1)]
house = []
chicken = []
brr = []
ans = []
answer = [987654321]
for z in range(1, N+1):
    nxn[z] = [0] + list(map(int, input().split()))

for i in range(1, N+1):
    for j in range(1, N+1):
        if nxn[i][j] == 1:
            house.append((i, j))
        if nxn[i][j] == 2:
            chicken.append((i, j))

dfs()
for i in range(len(ans)):
    check(i)

print(answer[0])