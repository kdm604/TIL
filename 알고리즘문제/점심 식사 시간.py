
def dfs(brr = []):
    if len(brr) == len(person)-1:
        tmp1 = ''
        tmp2 = ''
        for i in range(len(brr)):
            if brr[i] == 1:
                tmp1 += str(i+1) + ' '
            else:
                tmp2 += str(i+1) + ' '
        team.append((list(map(int, tmp1.split())), list(map(int, tmp2.split()))))
        return

    brr.append(1)
    dfs()
    brr.pop()
    brr.append(0)
    dfs()
    brr.pop()

T = int(input())

for test in range(T):
    N = int(input())
    nxn = [[0 for _ in range(N)]for _ in range(N)]
    person = [[]]
    gate = []
    team = []
    emptygate = [0, 0]
    ans = []
    for z in range(N):
        nxn[z] = list(input().split())

    for i in range(N):
        for j in range(N):
            if nxn[i][j] == '1':
                person.append((i, j))
            if nxn[i][j] > '1':
                gate.append((i, j))

    dfs()
    g1x = gate[0][0]
    g1y = gate[0][1]
    g2x = gate[1][0]
    g2y = gate[1][1]

    for i in range(len(team)):
        if i == 122:
            afas = 1
        timetable1 = []
        timetable2 = []
        if len(team[i][0]) > 0:
            for j in range(len(team[i][0])):
                x = person[team[i][0][j]][0]
                y = person[team[i][0][j]][1]
                x = abs(x-g1x) + abs(y-g1y)
                timetable1.append(x+1)

        if len(team[i][1]) > 0:
            for j in range(len(team[i][1])):
                x2 = person[team[i][1][j]][0]
                y2 = person[team[i][1][j]][1]
                x = abs(x2 - g2x) + abs(y2 - g2y)
                timetable2.append(x+1)

        timetable1.sort()
        timetable2.sort()


        index = 0
        cnt = 0
        while len(timetable1) > 0 and timetable1[-1] != 0:
            cnt += 1
            if emptygate[0] > 0:
                for w in range(index):
                    if cnt == timetable1[w]:
                        emptygate[0] -= 1
                        timetable1[w] = 0
            if len(timetable1) > 0:
                for w in range(index, len(timetable1)):
                    if emptygate[0] < 3:
                        if 0 < timetable1[w] <= cnt:
                            timetable1[w] = cnt + int(nxn[gate[0][0]][gate[0][1]])
                            emptygate[0] += 1
                            index += 1

        index2 = 0
        cnt2 = 0
        while len(timetable2) > 0 and timetable2[-1] != 0:
            cnt2 += 1
            if emptygate[1] > 0:
                for w in range(index2):
                    if cnt2 == timetable2[w]:
                        emptygate[1] -= 1
                        timetable2[w] = 0
            if len(timetable2) > 0:
                for w in range(index2, len(timetable2)):
                    if emptygate[1] < 3:
                        if 0 < timetable2[w] <= cnt2:
                            timetable2[w] = cnt2 + int(nxn[gate[1][0]][gate[1][1]])
                            emptygate[1] += 1
                            index2 += 1



        if cnt > cnt2:
            ans.append(cnt)
        if cnt <= cnt2:
            ans.append(cnt2)


    ans.sort()
    print("#%d %d" % (test+1, ans[0]))