T = int(input())

for test in range(T):

    A, B = map(int, input().split())

    print("#%d %d" % (test+1, A+B))