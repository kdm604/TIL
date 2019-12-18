import sys
sys.stdin = open("그림비교.txt")

N = int(input())
ans = []
tmp = 987654321
nxn = [[[0 for _ in range(7)] for _ in range(5)]for _ in range(N)]
c = 0
for z in range(5*N):
    if z % 5 == 0 and z != 0:
        c += 1

    nxn[c][(z % 5)] = list(sys.stdin.readline())

for n in range(N):
    for m in range(n+1, N):
        cnt = 0
        for i in range(5):
            for j in range(7):
                if nxn[n][i][j] != nxn[m][i][j]:
                    cnt += 1
        if cnt < tmp:
            tmp = cnt
            ans.clear()
            ans.append((n, m))


print(ans[0][0]+1, ans[0][1]+1)

