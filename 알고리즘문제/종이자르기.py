N, M = map(int, input().split())

row = [0]
col = [0]
maxx = 0
maxy = 0

cut = int(input())

for c in range(cut):
    d, xy = map(int, input().split())
    if d == 0:
        row.append(xy)
    else:
        col.append(xy)

row.append(M)
col.append(N)
row.sort()
col.sort()


for i in range(len(row)-1):
    y = abs(row[i] - row[i+1])
    if y > maxy:
        maxy = y
for i in range(len(col)-1):
    x = abs(col[i] - col[i+1])
    if x > maxx:
        maxx = x

print("%d" % (maxx * maxy))
