from collections import deque
import sys
input = sys.stdin.readline
dx = [1,0,-1,0]
dy = [0,1,0,-1]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

vis = [[False]*n for _ in range(n)]
color = 0

q_bridge = deque()
dist = [[-1]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and not vis[i][j]:
            q = deque()
            color += 1

            q.append((i, j))
            vis[i][j] = True
            board[i][j] = color

            while q:
                x, y = q.popleft()
                for a in range(4):
                    nx = x + dx[a]
                    ny = y + dy[a]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue
                    if vis[nx][ny]:
                        continue
                    if board[nx][ny] == 0:
                        q_bridge.append((x,y,color))
                        dist[x][y] = 0
                        continue
                    q.append((nx, ny))
                    vis[nx][ny] = True
                    board[nx][ny] = color

mn = 1e9

while q_bridge:
    x,y,c = q_bridge.popleft()
    for a in range(4):
        nx = x + dx[a]
        ny = y + dy[a]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if board[nx][ny] == c:
            continue
        if board[nx][ny] == 0:
            q_bridge.append((nx,ny,c))
            dist[nx][ny] = dist[x][y] + 1
            board[nx][ny] = c
        else:
            mn = min(mn, dist[x][y] + dist[nx][ny])

print(mn)