import sys
sys.stdin = open("게리멘더링.txt")
# 선거 구역을 2가지로 나누기 위해 부분집합으로 구역을 나눔
def dfs(brr = []):
    if len(brr) == N:
        tmp1 = ''
        tmp2 = ''
        for i in range(N):
            if brr[i] == 1:
                tmp1 += str(i+1) + ' '
            else:
                tmp2 += str(i + 1) + ' '
        if len(tmp1) > 0 and len(tmp2) > 0:
            team.append([list(map(int, tmp1.split())), list(map(int, tmp2.split()))])
        return

    brr.append(1)
    dfs()
    brr.pop()
    brr.append(0)
    dfs()
    brr.pop()

# 각 선거구의 구역들끼리 연결되어 있는지 체크하는 함수
def check(x, t):
    visited[x] = 1
    for y in range(1, N+1):
        if nxn[x][y] == 1 and visited[y] == 0:
            if y in team[i][t]:
                check(y, t)

N = int(input())
arr = [0] + list(map(int, input().split()))
nxn = [[0 for _ in range(N+1)]for _ in range(N+1)]
team = []
ans = 987654321
for i in range(1, N+1):
    A = list(map(int, input().split()))
    for j in range(len(A)):
        if j == 0:
            continue
        nxn[i][A[j]] = 1
        nxn[A[j]][i] = 1
dfs()

for i in range(len(team)):
    sum1 = 0
    sum2 = 0
    br = 0
    visited = [0 for _ in range(N+1)]
    check(team[i][0][0], 0)
    for q in range(len(team[i][0])):
        sum1 += arr[team[i][0][q]]
        if visited[team[i][0][q]] == 0:
            br = 1
            break
    if br == 1:
        continue

    visited = [0 for _ in range(N + 1)]
    check(team[i][1][0], 1)
    for q in range(len(team[i][1])):
        sum2 += arr[team[i][1][q]]
        if visited[team[i][1][q]] == 0:
            br = 1
            break
    if br == 1:
        continue

    tmp = abs(sum1 - sum2)

    if tmp < ans:
        ans = tmp

if ans == 987654321:
    print(-1)
else:
    print(ans)