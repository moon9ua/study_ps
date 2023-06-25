import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dp1 = [[0]*n for _ in range(n)] # 가로
dp2 = [[0]*n for _ in range(n)] # 세로
dp3 = [[0]*n for _ in range(n)] # 대각선

dp1[0][1] = 1

for i in range(0, n):
    for j in range(0, n):
        if j-1 >= 0 and board[i][j] == 0:
            dp1[i][j] += dp1[i][j-1] + dp3[i][j-1]
        if i-1 >= 0 and board[i][j] == 0:
            dp2[i][j] += dp2[i-1][j] + dp3[i-1][j]
        if i-1 >= 0 and j-1 >= 0 and board[i-1][j] == 0 \
            and board[i][j-1] == 0 and board[i][j] == 0:
            dp3[i][j] += dp1[i-1][j-1] + dp2[i-1][j-1] + dp3[i-1][j-1]

print(dp1[n-1][n-1] + dp2[n-1][n-1] + dp3[n-1][n-1])