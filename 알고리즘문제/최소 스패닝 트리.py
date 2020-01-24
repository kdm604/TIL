def find_set(x):
    if x == p[x]:
        return x
    else:
        tmp = find_set(p[x])
        p[x] = tmp
        return tmp

def union(x, y):
    p[find_set(x)] = find_set(y)

def kruskal():
    cnt = 0
    for i in GE:
        if cnt == V - 1:
            return
        if find_set(i[0]) != find_set(i[1]):
            union(i[0], i[1])
            ans[0] += i[2]
            cnt += 1

T = int(input())
for test in range(T):
    V, E = map(int, input().split())
    GE = []
    ans = [0]
    p = [i for i in range(V+1)]
    for z in range(E):
        a, b, w = map(int, input().split())
        GE.append((a, b, w))


    GE = sorted(GE, key=lambda s:s[2])

    kruskal()

    print("#%d %d" % (test+1, ans[0]))