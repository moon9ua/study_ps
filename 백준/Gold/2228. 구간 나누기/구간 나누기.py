import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]

ps = [0] * (n+1)
for i in range(1, n+1):
    ps[i] = ps[i-1] + nums[i-1]

dp = [[0]*(m+1) for _ in range(n+1)]
for j in range(1, m+1):
    dp[0][j] = -1e9

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j]
        for k in range(1, i+1):
            if k >= 2:
                dp[i][j] = max(dp[i][j], dp[k-2][j-1] + ps[i] - ps[k-1])
            elif k == 1 and j == 1:
                dp[i][j] = max(dp[i][j], ps[i])

print(dp[n][m])