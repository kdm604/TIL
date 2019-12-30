N, K = map(int, input().split())
ans = 0
dp = [[0 for _ in range(201)]for _ in range(201)]

dp[0][0] = 1

for i in range(1, K+1):
    for j in range(N+1):
        for z in range(j+1):
            dp[i][j] += dp[i - 1][j - z]
            dp[i][j] %= 1000000000

print(dp[K][N])