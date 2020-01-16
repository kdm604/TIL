def dfs(pri, month):
    global ans
    if month >= 13:
        ans = min(ans, pri)

    else:
        if visited[month]:
            dfs(pri + price[0] * visited[month], month + 1)
            dfs(pri + price[1], month + 1)
            dfs(pri + price[2], month + 3)

        else:
            dfs(pri, month+1)

T = int(input())
for test in range(T):
    price = list(map(int, input().split()))
    visited = [0] + list(map(int, input().split()))
    ans = 987654321

    dfs(0, 1)

    if ans < price[3]:
        print("#%d %d" % (test+1, ans))
    else:
        print("#%d %d" % (test+1, price[3]))