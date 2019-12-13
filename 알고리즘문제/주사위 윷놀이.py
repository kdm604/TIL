import sys
sys.stdin = open("주사위 윷놀이.txt")
# 10번의 이동 기회를 이용하여 최대점수를 찾는 문제
# 코너(파란색 원)의 위치일때는 이동방향 설정이 필요함.
# 시작부터 도착까지의 이동 경로는 4가지가 있음.
# 말은 4개 이동위치에 다른말이 있다면 이동불가.

# 순열로 1~4번말을 이동할 주사위 배치하기
def dfs():
    if len(brr) == 10:
        team = []
        tmp = ''
        player = []
        bb = 0
        for z in range(10):
            tmp += str(brr[z]) + ' '
        team = list(map(int, tmp.split()))

        score = 0
        bb = 0
        player = [0 for _ in range(5)]
        mal = [[0 for _ in range(2)] for _ in range(5)]
        for j in range(len(team)):

            mal[team[j]][0] += arr[j]

            if mal[team[j]][1] == 0:
                if mal[team[j]][0] > 20:
                    score += way[0]
                    player[team[j]] = pan[0]
                else:
                    score += way[mal[team[j]][0]]
                    player[team[j]] = pan[mal[team[j]][0]]

            if mal[team[j]][1] == 0:
                if mal[team[j]][0] == 5:
                    mal[team[j]][1] = 1
                    mal[team[j]][0] = 0

                if mal[team[j]][0] == 10:
                    mal[team[j]][1] = 2
                    mal[team[j]][0] = 0

                if mal[team[j]][0] == 15:
                    mal[team[j]][1] = 3
                    mal[team[j]][0] = 0


            if mal[team[j]][1] == 1:
                if mal[team[j]][0] >= 8:
                    score += way1[0]
                    player[team[j]] = pan1[0]
                else:
                    score += way1[mal[team[j]][0]]
                    player[team[j]] = pan1[mal[team[j]][0] + 1]

            if mal[team[j]][1] == 2:
                if mal[team[j]][0] >= 7:
                    score += way2[0]
                    player[team[j]] = pan2[0]
                else:
                    score += way2[mal[team[j]][0]]
                    player[team[j]] = pan2[mal[team[j]][0] + 1]

            if mal[team[j]][1] == 3:
                if mal[team[j]][0] >= 8:
                    score += way3[0]
                    player[team[j]] = pan3[0]

                else:
                    score += way3[mal[team[j]][0]]
                    player[team[j]] = pan3[mal[team[j]][0] + 1]

            for p in range(1, 4):
                for o in range(p + 1, 5):
                    if player[p] == player[o] and player[p] != 0:
                        bb = 1
            if bb == 1:
                break

        if bb == 0 and score > ans[0]:
            ans[0] = score


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

# 윷놀이판에 있는 말들의 위치가 겹치는 경우를 탐색하기 위해 pan 배열 생성
pan = [i for i in range(21)]
pan1 = [0, 5, 21, 22, 23, 24, 25, 26, 20]
pan2 = [0, 10, 27, 28, 24, 25, 26, 20]
pan3 = [0, 15, 29, 30, 31, 24, 25, 26, 20]


# 말들이 이동할 수 있는 경로들의 스코어들
way = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40] # 0 ~ 19번
way1 = [0, 13, 16, 19, 25, 30, 35, 40] # 4 20 21 22 23 24 25 19
way2 = [0, 22, 24, 25, 30, 35, 40] # 9 26 27 23 24 25 19
way3 = [0, 28, 27, 26, 25, 30, 35, 40] # 14 28 29 30 23 24 25 19


arr = list(map(int, input().split()))
brr = []
team = []
ans = [0]
dfs()


print(ans[0])