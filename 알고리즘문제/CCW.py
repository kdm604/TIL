import sys

p = []

for i in range(3):
    x, y = map(int, input().split())
    p.append([x, y])

a = p[0][0] - p[1][0]
b = p[0][1] - p[1][1]

c = p[1][0] - p[2][0]
d = p[1][1] - p[2][1]

ans = (a*d)-(b*c)

if ans == 0:
    print(0)
if ans > 0:
    print(1)
if ans < 0:
    print(-1)