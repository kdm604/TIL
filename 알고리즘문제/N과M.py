import sys
sys.stdin = open("N과 M.txt")

def dfs(x, depth):
    brr.append(x)
    if depth == M:
        for z in range(M):
            print(brr[z], end=' ')
        print()
        return
    for j in range(x, N+1):
        if j not in brr:
            dfs(j, depth+1)
            brr.pop()

N, M = map(int, input().split())

for i in range(1, N+1):
    brr = []
    dfs(i, 1)

