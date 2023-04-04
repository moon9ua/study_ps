import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*m for _ in range(n)]
left = [[0]*m for _ in range(n)]
right = [[0]*m for _ in range(n)]

dp[0][0] = board[0][0]
for j in range(1, m):
    dp[0][j] = dp[0][j-1] + board[0][j]

for i in range(1, n):
    left[i][0] = dp[i-1][0] + board[i][0]
    for j in range(1, m):
        left[i][j] = max(dp[i-1][j], left[i][j-1]) + board[i][j]
    
    right[i][m-1] = dp[i-1][m-1] + board[i][m-1]
    for j in range(m-2, -1, -1):
        right[i][j] = max(dp[i-1][j], right[i][j+1]) + board[i][j]

    for j in range(m):
        dp[i][j] = max(left[i][j], right[i][j])

print(dp[-1][-1])