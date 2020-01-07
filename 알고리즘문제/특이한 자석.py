from collections import deque

def turn(x, left, right):
    lx = x - 1
    rx = x + 1

    if lx >= 0 and left == 1:
        if nxm[lx][2] != nxm[x][6]:
            check[lx] = 1
            turn(lx, 1, 0)

    if rx < 4 and right == 1:
        if nxm[rx][6] != nxm[x][2]:
            check[rx] = 1
            turn(rx, 0, 1)



T = int(input())


# arr 배열에 첫번째 요소는 자석의 번호 두번째는 회전방향

for test in range(T):
    K = int(input())
    arr = []
    nxm = [deque() for _ in range(4)]

    ans = 0

    for i in range(4):
        nxm[i] = deque(list(map(int, input().split())))

    for i in range(K):
        a, b = map(int, input().split())
        arr.append((a, b))

    cnt = 0
    while len(arr):
        check = [0 for _ in range(4)]
        direction = [0 for _ in range(4)]
        num, dir = arr.pop(0)
        check[num-1] = 1
        direction[num-1] = dir

        # 회전을 하게된다면 어떤방향으로 회전해야하는지 방향을 지정해주는 while문
        while 1:
            cnt = 0
            for i in range(4):
                if direction[i] == 0:
                    li = i - 1
                    ri = i + 1

                    if 0 <= li:
                        if direction[li] == 1:
                            direction[i] = -1
                        if direction[li] == -1:
                            direction[i] = 1
                    if ri < 4:
                        if direction[ri] == 1:
                            direction[i] = -1
                        if direction[ri] == -1:
                            direction[i] = 1

                if direction[i] == 0:
                    cnt += 1
            if cnt == 0:
                break

        turn(num-1, 1, 1)

        for i in range(4):
            if check[i] == 1:
                if direction[i] == 1:
                    tmp = nxm[i].pop()
                    nxm[i].appendleft(tmp)

                if direction[i] == -1:
                    tmp = nxm[i].popleft()
                    nxm[i].append(tmp)


    for i in range(4):
        if nxm[i][0] == 1:
            if i == 0:
                ans += 1
            elif i == 1:
                ans += 2
            elif i == 2:
                ans += 4
            elif i == 3:
                ans += 8

    print("#%d %d" % (test+1, ans))