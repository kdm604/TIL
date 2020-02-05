dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, cnt, tmp):
    tmp += str(nxn[x][y])
    if cnt == 7:
        ans.append(tmp)
        return

    for d in range(4):
        if nxn[x + dx[d]][y + dy[d]] >= 0:
            dfs(x + dx[d], y + dy[d], cnt + 1, tmp)


T = int(input())
for test in range(T):

    nxn = [[-1 for _ in range(6)] for _ in range(6)]
    ans = []

    for z in range(1, 5):
        nxn[z] = [-1] + list(map(int, input().split())) + [-1]

    for i in range(1, 5):
        for j in range(1, 5):
            tmp = ""
            dfs(i, j, 1, tmp)

    ans = list(set(ans))

    answer = len(ans)

    print("#%d %d" % (test + 1, answer))