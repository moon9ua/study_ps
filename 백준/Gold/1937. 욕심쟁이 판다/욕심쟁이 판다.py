import sys
input = sys.stdin.readline
dx = [1,0,-1,0]
dy = [0,1,0,-1]
sys.setrecursionlimit(111111)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1]*n for _ in range(n)]

def dfs(x, y):
    if dp[x][y] == -1:
        dp[x][y] = 1
        tmp = 0
        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]
            if not 0 <= nx < n or not 0 <= ny < n:
                continue
            if board[nx][ny] > board[x][y]:
                tmp = max(tmp, dfs(nx, ny))
        dp[x][y] += tmp
    return dp[x][y]

ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))

print(ans)