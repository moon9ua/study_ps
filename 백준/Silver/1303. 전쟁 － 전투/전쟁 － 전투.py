from collections import deque
import sys
input = sys.stdin.readline
dx = [1,0,-1,0]
dy = [0,1,0,-1]

m,n = map(int,input().split())
board = [input().rstrip() for _ in range(n)]

tot_w,tot_b = 0,0
q = deque()
vis = [[False]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if not vis[i][j]:
            q.append((i,j))
            vis[i][j] = True
            cnt = 1
            while q:
                x,y = q.popleft()
                for a in range(4):
                    nx = x + dx[a]
                    ny = y + dy[a]
                    if not 0<=nx<n or not 0<=ny<m:
                        continue
                    if board[nx][ny] != board[x][y] or vis[nx][ny]:
                        continue
                    q.append((nx,ny))
                    vis[nx][ny] = True
                    cnt += 1
            if board[i][j] == 'W':
                tot_w += cnt**2
            else:
                tot_b += cnt**2

print(tot_w, tot_b)