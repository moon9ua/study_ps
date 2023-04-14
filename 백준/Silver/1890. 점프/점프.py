import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break
        if dp[i][j]:
            jump = board[i][j]
            for nx,ny in [(i+jump,j), (i,j+jump)]:
                if not 0<=nx<n or not 0<=ny<n:
                    continue
                dp[nx][ny] += dp[i][j]

print(dp[-1][-1])