T = int(input())

for test in range(T):
    A, B, C = map(int, input().split())

    if A > B:
        print("#%d %d" % (test+1, C//B))
    else:
        print("#%d %d" % (test+1, C//A))