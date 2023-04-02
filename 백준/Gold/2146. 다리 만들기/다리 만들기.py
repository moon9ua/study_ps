from collections import deque
import sys

input = sys.stdin.readline
dx = [1,0,-1,0]
dy = [0,1,0,-1]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
color = [[0]*n for _ in range(n)]

num = 1
for i in range(n):
    for j in range(n):
        if not color[i][j] and board[i][j]:
            color[i][j] = num
            q = deque()
            q.append((i,j))
            while q:
                x,y = q.popleft()
                for a in range(4):
                    nx = x + dx[a]
                    ny = y + dy[a]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue
                    if color[nx][ny] or board[nx][ny] == 0:
                        continue
                    color[nx][ny] = num
                    q.append((nx,ny))
        num += 1

def check(i,j):
    if board[i][j] == 0:
        return False
    zero = 0
    for a in range(4):
        ni = i + dx[a]
        nj = j + dy[a]
        if ni < 0 or nj < 0 or ni >= n or nj >= n:
            continue
        if board[ni][nj]:
            continue
        zero += 1
    return bool(zero)

ans = 1e9
for i in range(n):
    for j in range(n):
        if check(i,j):
            now = color[i][j]
            vis = [[-1]*n for _ in range(n)]
            vis[i][j] = 0
            q = deque()
            q.append((i,j))
            while q:
                x,y = q.popleft()
                if color[x][y] != 0 and color[x][y] != now:
                    ans = min(ans, vis[x][y]-1)
                    break
                for a in range(4):
                    nx = x + dx[a]
                    ny = y + dy[a]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue
                    if color[nx][ny] == now or vis[nx][ny] != -1:
                        continue
                    vis[nx][ny] = vis[x][y] + 1
                    q.append((nx,ny))

print(ans)