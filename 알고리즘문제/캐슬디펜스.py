import sys
import copy
from collections import deque
sys.stdin = open("캐슬디펜스.txt")
# 적들이 한턴에 한칸씩 내려옴. 턴이 지나면 모든 적들을 한칸씩 당겨야함
# 궁수는 D거리 이하의 적만 공격가능. 여럿일 경우 가장 가까운 적 -> 왼쪽
# 궁수배치를 조합으로 뽑아서 배치 적들을 제거한 후에 최대값 출력

def comb(n, r):
    if r == 0:
        tmp = ''
        for i in range(3):
            tmp += str(test[i]) + ' '
        team.append(list(map(int, tmp.split())))
        return
    elif n < r:
        return
    else:
        test[r-1] = arr[n-1]
        comb(n-1, r-1)
        comb(n-1, r)

def bfs(fx, fy):
    Q = deque()
    Q.append((fx, fy))

    while Q:
        x, y = Q.popleft()
        if abs(x - fx) + abs(y - fy) > D:
            break
        if (x != fx or y != fy) and nxm[x][y] == 1:
            kill.append((x, y))
            break
        for d in range(3):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                Q.append((nx, ny))

dx = [0, -1, 0]
dy = [-1, 0, 1]

N, M, D = map(int, input().split())

nxm2 = [[0 for _ in range(M)] for _ in range(N+1)]
arr = [i for i in range(M)]
test = [0 for _ in range(3)]
team = []
kill = []
answer = 0
for z in range(N):
    nxm2[z] = list(map(int, input().split()))

comb(M, 3)

for z in range(len(team)):
    nxm = copy.deepcopy(nxm2)
    kill = []
    nxm[N] = [0] * M
    nxm[N][team[z][0]] = 2
    nxm[N][team[z][1]] = 2
    nxm[N][team[z][2]] = 2
    ans = 0

    br = 0
    while br == 0:
        bfs(N, team[z][0])
        bfs(N, team[z][1])
        bfs(N, team[z][2])

        for p in range(len(kill)):
            x, y = kill.pop()
            if nxm[x][y] == 1:
                ans += 1
                nxm[x][y] = 0

        nxm[N-1] = [0] * M
        for x in range(N-2, -1, -1):
            for y in range(M):
                if nxm[x][y] == 1:
                    nxm[x][y] = 0
                    nxm[x+1][y] = 1

        cnt = 0
        for x in range(N):
            for y in range(M):
                if nxm[x][y] == 1:
                    cnt += 1
        if cnt == 0:
            break

    if ans > answer:
        answer = ans

print(answer)
