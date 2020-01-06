# 결국 직사각형을 찍는 문제기때문에 가로, 세로의 길이를 한번씩만 구하고 2번 사용하면 됨.
# ex 가로->세로->가로->세로
# 그래서 세로 써치가능범위 mx  // 가로 써치가능범위 my를 측정해서
# 포문으로 mx,my를 돌리면서 지나가는 길에 있는 2차원 배열값을 tmp리스트에 넣고
# arr 배열에 tmp의 길이와 tmp의 요소들을 튜플 형태로 넣어줌
# arr 배열을 내림차순정렬 한 후에 디저트를 전부 다른걸 들고있는 녀석이 나온다면
# 길이를 ans에 넣어주고 포문을 끝냄

T = int(input())

for test in range(T):
    N = int(input())
    nxn = [[0 for _ in range(N)] for _ in range(N)]
    arr = []
    ans = -1
    for i in range(N):
        nxn[i] = list(map(int, input().split()))

    for x in range(N):
        for y in range(N):
            mx = 0
            my = 0
            tx = x
            ty = y
            # mx 즉 사각형 그릴때  0 or 2번째 범위를 측정
            for lx in range(1, 21):
                nx = x + lx
                if nx == N:
                    mx = lx - 1
                    break
            # my 즉 사각형 그릴때  1 or 3번째 범위를 측정
            for ly in range(1, 21):
                ny = y - ly
                if ny < 0:
                    my = ly - 1
                    break
            # 4가지 범위가 1이상이 되어야 가장작은 싸이클이 나오기때문에 최소값을 둘다 1로 설정
            if mx > 0 and my > 0:
                for lx in range(1, mx + 1):
                    for ly in range(1, my + 1):
                        tmp = []
                        px = tx
                        py = ty
                        br = 0

                        # 나의 사각형 만들기는 오른쪽아래 -> 왼쪽 아래 -> 왼쪽 위 -> 오른쪽 위 를 그리며 탐색
                        for i in range(4):
                            if i == 0:
                                for w in range(lx):
                                    nx = px + 1
                                    ny = py + 1
                                    if 0 <= nx < N and 0 <= ny < N:
                                        tmp.append(nxn[nx][ny])
                                        px = nx
                                        py = ny
                                    else:
                                        br = 1
                                        break
                            elif i == 1:
                                for w in range(ly):
                                    nx = px + 1
                                    ny = py - 1
                                    if 0 <= nx < N and 0 <= ny < N:
                                        tmp.append(nxn[nx][ny])
                                        px = nx
                                        py = ny
                                    else:
                                        br = 1
                                        break
                            elif i == 2:
                                for w in range(lx):
                                    nx = px - 1
                                    ny = py - 1
                                    if 0 <= nx < N and 0 <= ny < N:
                                        tmp.append(nxn[nx][ny])
                                        px = nx
                                        py = ny
                                    else:
                                        br = 1
                                        break
                            elif i == 3:
                                for w in range(ly):
                                    nx = px - 1
                                    ny = py + 1
                                    if 0 <= nx < N and 0 <= ny < N:
                                        tmp.append(nxn[nx][ny])
                                        px = nx
                                        py = ny
                                    else:
                                        br = 1
                                        break
                        if br == 0:
                            tmp2 = len(tmp)
                            arr.append((tmp2, tmp))

    arr.sort(reverse=True)

    for i in range(len(arr)):
        visited = [0 for _ in range(101)]
        for j in range(len(arr[i][1])):
            visited[arr[i][1][j]] += 1
        cnt = max(visited)
        # if i ==
        if cnt < 2:
            ans = arr[i][0]
            break

    print("#%d %d" % (test + 1, ans))
