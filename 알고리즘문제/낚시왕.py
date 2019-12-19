import sys
sys.stdin = open("낚시왕.txt")
#d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미한다.
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]
R, C, M = map(int, input().split())
# 체크배열을 통해 이동해야하는 상어와 이동하지 않아도 되는 상어를 구분 ex) 이미 잡혔거나 다른상어에게 먹힌 경우 제외
check = [0 for _ in range(M+1)]
sharks = [[0]]
nxm = [[0 for _ in range(C+1)]for _ in range(R+1)]
ans = 0
for i in range(1, M+1):
    r, c, s, d, z = map(int, input().split())
    nxm[r][c] = i
    #샤크 배열에는 좌표(r,c), 속도, 방향, 크기, 그리고 상어번호로 저장
    sharks.append([r, c, s, d, z, i])
cnt = 0
if M > 0:
    while cnt < C:
        br = 0
        cnt += 1
        for j in range(1, R+1):
            if nxm[j][cnt] > 0:
                check[nxm[j][cnt]] = 1
                ans += sharks[nxm[j][cnt]][4]
                nxm[j][cnt] = 0
                br = 1
                break

        # 낚시꾼이 땅에서 가장 가까운 상어를 잡는 코드 + 잡은 상어의 크기를 ans에 더하고 check배열에 잡은 상어 체크

        # 상어들 이동
        for i in range(1, len(sharks)):
            if check[i] == 1:
                continue
            x = sharks[i][0]
            y = sharks[i][1]
            nxm[x][y] = 0

            pp = sharks[i][2]
            cyr = R*2 - 2
            cyc = C*2 - 2
            if 1 <= sharks[i][3] <= 2 and pp >= cyr:
                pp %= cyr
            if 3 <= sharks[i][3] <= 4 and pp >= cyc:
                pp %= cyc
            for j in range(pp):
                x = sharks[i][0]
                y = sharks[i][1]
                #상어의 이동이 수직이동 일때 방향을 바꿔주는 코드
                if 1 <= sharks[i][3] <= 2:
                    if sharks[i][0] == 1 and sharks[i][3] == 1:
                        sharks[i][3] = 2
                    elif sharks[i][0] == R and sharks[i][3] == 2:
                        sharks[i][3] = 1

                # 상어의 이동이 수평이동 일때 방향을 바꿔주는 코드
                elif 3 <= sharks[i][3] <= 4:
                    if sharks[i][1] == 1 and sharks[i][3] == 4:
                        sharks[i][3] = 3
                    elif sharks[i][1] == C and sharks[i][3] == 3:
                        sharks[i][3] = 4
                sharks[i][0] = x + dx[sharks[i][3]]
                sharks[i][1] = y + dy[sharks[i][3]]

        for i in range(1, len(sharks)):
            if check[i] == 1:
                continue
            x = sharks[i][0]
            y = sharks[i][1]

            if nxm[x][y] == 0:
                nxm[x][y] = sharks[i][5]
            else:
                if sharks[nxm[x][y]][4] > sharks[i][4]:
                    check[sharks[i][5]] = 1
                else:
                    check[nxm[x][y]] = 1
                    nxm[x][y] = sharks[i][5]

print(ans)

