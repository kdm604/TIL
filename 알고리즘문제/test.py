import sys
sys.stdin = open("text.txt")
arr = [[], [], []]
for i in range(1, 21):
    arr[0].append(2*i)
for i in range(4):
    arr[1].append(10 + (3*i))
for i in range(4):
    arr[1].append(25 + i)
arr[1].append(30)
for i in range(3):
    arr[2].append(20 + (2 * i))
for i in range(4):
    arr[2].append(25 + (5 * i))


def travel(now_loc, dis):
    if now_loc == (1, 4, 0):
        now_loc = (2, 0, 0)
    elif now_loc == (1, 9, 0):
        now_loc = (3, 0, 0)
    elif now_loc == (1, 14, 0):
        now_loc = (2, 8, 1)
    elif now_loc == (2, 4, 0) or now_loc == (2, 4, 1):
        now_loc = (3, 3, 0)
    elif now_loc == (2, 8, 0):
        now_loc = (1, 14, 0)

    if now_loc[0] == 1:
        if 20 - now_loc[1] <= dis:
            return -1, 0, 0
        else:
            return 1, now_loc[1] + dis, 0

    elif now_loc[0] == 2 and now_loc[2] == 0:
        if 5 - now_loc[1] <= dis:
            return travel((3, 3, 0), dis - (4 - now_loc[1]))
        return 2, now_loc[1] + dis, 0

    elif now_loc[0] == 2 and now_loc[2] == 1:
        if now_loc[1] - dis - 4 < 0:
            return travel((3, 3, 0), dis - (now_loc[1] - 4))
        return 2, now_loc[1] - dis, 1

    else:
        if 7 - now_loc[1] <= dis:
            return -1, 0, 0
        else:
            return 3, now_loc[1] + dis, 0


inp = list(map(int, input().split()))
max_num = 0
loc_list = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]


def change_loc(loc):
    if loc[0] == 0:
        return 30   # trash value

    if loc[0] == 1:
        return loc[1]
    if loc[0] == 2 and loc[1] == 0:
        return 4
    if loc[0] == 2 and loc[1] == 8:
        return 14
    if loc[0] == 3 and loc[1] == 0:
        return 9
    if loc[0] == 3 and loc[1] == 6:
        return 19
    if loc[0] == 2:
        return 19 + loc[1]
    if loc[0] == 3 and loc[1] == 3:
        return 23
    if loc[0] == 3 and loc[1] < 3:
        return 26 + loc[1]
    else:
        return 24 + loc[1]


ck_list = [False] * 31
max_number = 0


def pick_one(cnt, score):
    global loc_list, inp, arr, max_number
    if cnt == 10:
        if score > max_number:
            max_number = score
        return
    dis = inp[cnt]
    for ind in range(4):
        if ind > cnt:
            continue
        if loc_list[ind][0] != -1:
            temp_loc = loc_list[ind][:]
            temp_dis = dis
            if loc_list[ind][0] == 0:
                temp_dis = dis - 1
                new_loc = (1, 0, 0)
            else:
                new_loc = temp_loc[:]
            new_loc = travel(new_loc, temp_dis)
            if new_loc[0] != -1 and ck_list[change_loc((new_loc[0], new_loc[1]))]:
                pass
            else:
                if new_loc[0] == -1:
                    loc_list[ind] = new_loc
                    ck_list[change_loc((temp_loc[0], temp_loc[1]))] = False
                    pick_one(cnt+1, score)
                    ck_list[change_loc((temp_loc[0], temp_loc[1]))] = True
                    loc_list[ind] = temp_loc
                else:
                    loc_list[ind] = new_loc
                    ck_list[change_loc((new_loc[0], new_loc[1]))] = True
                    ck_list[change_loc((temp_loc[0], temp_loc[1]))] = False
                    new_score = score + arr[new_loc[0] - 1][new_loc[1]]
                    pick_one(cnt+1, new_score)
                    loc_list[ind] = temp_loc
                    ck_list[change_loc((new_loc[0], new_loc[1]))] = False
                    ck_list[change_loc((temp_loc[0], temp_loc[1]))] = True


pick_one(0, 0)
print(max_number)
