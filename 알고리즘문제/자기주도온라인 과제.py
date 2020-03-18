import sys
sys.stdin = open("자기주도온라인 과제.txt")

year = int(input())
month = int(input())

day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


if year % 4 == 0 and year % 100 != 0 and month == 2:
    print(day[month] + 1)

elif year % 400 == 0 and month == 2:
    print(day[month] + 1)

else:
    print(day[month])