def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(p[x])

def union(x, y):
    a = find_set(x)
    b = find_set(y)

    if a < b:
        p[b] = a
    else:
        p[a] = b


T = int(input())
for test in range(T):
    N, M = map(int, input().split())
    p = [i for i in range(N+1)]
    tmp = ""

    for z in range(M):
        o, a, b = map(int, input().split())
        if o == 0:
            union(a, b)

        if o == 1:
            if find_set(a) == find_set(b):
                tmp += '1'
            else:
                tmp += '0'

    print("#%d %s" % (test+1, tmp))

