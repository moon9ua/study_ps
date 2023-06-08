import sys
input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

r, c = map(int, input().split())
board = [input().rstrip() for _ in range(r)]

def dfs(x, y):
    global mx, path

    for a in range(4):
        nx = x + dx[a]
        ny = y + dy[a]
        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue
        if board[nx][ny] in path:
            continue
        path += board[nx][ny]
        mx = max(mx, len(path))
        dfs(nx, ny)
        path = path[:-1]
    
mx = 1
path = board[0][0]
dfs(0, 0)

print(mx)