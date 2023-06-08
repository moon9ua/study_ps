import sys
input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

r, c = map(int, input().split())
board = [input().rstrip() for _ in range(r)]

def dfs(x, y, k):
    global mx

    for a in range(4):
        nx = x + dx[a]
        ny = y + dy[a]
        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue
        if used[ord(board[nx][ny])]:
            continue
        used[ord(board[nx][ny])] = True
        mx = max(mx, k+1)
        dfs(nx, ny, k+1)
        used[ord(board[nx][ny])] = False
    
used = [False] * 200
used[ord(board[0][0])] = True
mx = 1
dfs(0, 0, 1)

print(mx)