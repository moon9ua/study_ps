import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

ps = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        ps[i][j] = board[i-1][j-1] + ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split()) # 1-idx
    ans = ps[x2][y2] - ps[x1-1][y2] - ps[x2][y1-1] + ps[x1-1][y1-1]
    print(ans)