import sys
import copy
sys.stdin = open("감시.txt")

# cctv가 8개까지 8개의 cctv를 각자 4방향 돌린 모든방법중에 감시가 되는 최대 갯수 구하기
# 1~5 는 cctv 6은 벽 // 1~4 까지의 cctv 방향을 다 돌려봐야됨. 5번은 4방향이라 항상 최대써치
# cctv에 5번을 제외한 cctv를 넣고 순열로 1~4방향을 지정해서 써치범위 탐색

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# cctv의 방향들의 순열을 만들어서 ans배열에 전부 저장
def dfs():
    if len(brr) == len(cctv):
        tmp = ''
        for i in range(len(cctv)):
            tmp += str(brr[i]) + ' '
        ans.append(list(map(int, tmp.split())))
        return

    brr.append(1)
    dfs()
    brr.pop()
    brr.append(2)
    dfs()
    brr.pop()
    brr.append(3)
    dfs()
    brr.pop()
    brr.append(4)
    dfs()
    brr.pop()

N, M = map(int, input().split())
brr = []
nxm = [[0 for _ in range(M)] for _ in range(N)]
ans = []
cnt = 0
answer = 98754321
for z in range(N):
    nxm[z] = list(map(int, input().split()))

cctv = []
cctv2 = []
wall = 0
# 1~4 까지의 cctv들을 cctv배열에 저장 5번 cctv를 cctv2배열에 저장
for x in range(N):
    for y in range(M):
        if 0 < nxm[x][y] <= 4:
            cctv.append((x, y))
        if nxm[x][y] == 5:
            cctv2.append((x, y))
        if nxm[x][y] == 6:
            wall += 1
dfs()

nxm3 = [[0 for _ in range(M)] for _ in range(N)]
for p in range(len(cctv2)):
    for d in range(4):
        for e in range(1, 9):
            nx = cctv2[p][0] + dx[d] * e
            ny = cctv2[p][1] + dy[d] * e

            if 0 <= nx < N and 0 <= ny < M:
                if nxm[nx][ny] == 6:
                    break
                else:
                    nxm3[nx][ny] = 7
            else:
                break

for z in range(len(ans)):
    nxm2 = copy.deepcopy(nxm3)
    for w in range(len(cctv)):
        # 1번 cctv 일떄
        if nxm[cctv[w][0]][cctv[w][1]] == 1:
            for e in range(1, 9):
                nx = cctv[w][0] + dx[ans[z][w] - 1] * e
                ny = cctv[w][1] + dy[ans[z][w] - 1] * e
                if 0 <= nx < N and 0 <= ny < M:
                    if nxm[nx][ny] == 6:
                        br = 1
                        break
                    nxm2[nx][ny] = 7
                else:
                    break

        # 2번 cctv 일때
        if nxm[cctv[w][0]][cctv[w][1]] == 2:
            for e in range(1, 9):
                nx = cctv[w][0] + dx[ans[z][w] - 1] * e
                ny = cctv[w][1] + dy[ans[z][w] - 1] * e
                if 0 <= nx < N and 0 <= ny < M:
                    if nxm[nx][ny] == 6:
                        br = 1
                        break
                    nxm2[nx][ny] = 7
                else:
                    break

            for e in range(1, 9):
                nx = cctv[w][0] + dx[(ans[z][w] + 1) % 4] * e
                ny = cctv[w][1] + dy[(ans[z][w] + 1) % 4] * e
                if 0 <= nx < N and 0 <= ny < M:
                    if nxm[nx][ny] == 6:
                        br = 1
                        break
                    nxm2[nx][ny] = 7
                else:
                    break

        # 3번 cctv 일때
        if nxm[cctv[w][0]][cctv[w][1]] == 3:
            for e in range(1, 9):
                nx = cctv[w][0] + dx[ans[z][w] - 1] * e
                ny = cctv[w][1] + dy[ans[z][w] - 1] * e
                if 0 <= nx < N and 0 <= ny < M:
                    if nxm[nx][ny] == 6:
                        br = 1
                        break
                    nxm2[nx][ny] = 7
                else:
                    break

            for e in range(1, 9):
                nx = cctv[w][0] + dx[(ans[z][w]) % 4] * e
                ny = cctv[w][1] + dy[(ans[z][w]) % 4] * e
                if 0 <= nx < N and 0 <= ny < M:
                    if nxm[nx][ny] == 6:
                        br = 1
                        break
                    nxm2[nx][ny] = 7
                else:
                    break

        # 4번 cctv 일때
        if nxm[cctv[w][0]][cctv[w][1]] == 4:
            for e in range(1, 9):
                nx = cctv[w][0] + dx[ans[z][w] - 1] * e
                ny = cctv[w][1] + dy[ans[z][w] - 1] * e
                if 0 <= nx < N and 0 <= ny < M:
                    if nxm[nx][ny] == 6:
                        br = 1
                        break
                    nxm2[nx][ny] = 7
                else:
                    break

            for e in range(1, 9):
                nx = cctv[w][0] + dx[(ans[z][w]) % 4] * e
                ny = cctv[w][1] + dy[(ans[z][w]) % 4] * e
                if 0 <= nx < N and 0 <= ny < M:
                    if nxm[nx][ny] == 6:
                        br = 1
                        break
                    nxm2[nx][ny] = 7
                else:
                    break

            for e in range(1, 9):
                nx = cctv[w][0] + dx[(ans[z][w] + 1) % 4] * e
                ny = cctv[w][1] + dy[(ans[z][w] + 1) % 4] * e
                if 0 <= nx < N and 0 <= ny < M:
                    if nxm[nx][ny] == 6:
                        br = 1
                        break
                    nxm2[nx][ny] = 7
                else:
                    break

        cnt = 0
        for k in range(N):
            for l in range(M):
                if nxm2[k][l] == 0 and nxm[k][l] == 0:
                    cnt += 1

        if answer > cnt:
            answer = cnt
if len(cctv) == 0 and len(cctv2) == 0:
    answer = N * M - wall

for k in range(N):
    for l in range(M):
        if nxm2[k][l] == 0 and nxm[k][l] == 0:
            cnt += 1
if answer > cnt:
    answer = cnt

print(answer)