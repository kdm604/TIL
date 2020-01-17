T = int(input())
r = []
for test in range(T):
    a, b, c, d = map(int, input().split())

    x = a / b
    y = c / d

    if x == y:
        r.append("#%d DRAW" % (test + 1))
    elif x > y:
        r.append("#%d ALICE" % (test + 1))
    else:
        r.append("#%d BOB" % (test + 1))

print('\n'.join(r))