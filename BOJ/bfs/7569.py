from collections import deque
import sys
input = sys.stdin.readline
dx = [1,0,0,-1,0,0]
dy = [0,1,0,0,-1,0]
dz = [0,0,1,0,0,-1]

m,n,h = map(int, input().split())
board = [[input().rstrip().split() for _ in range(n)] for _ in range(h)]

rest = m*n*h
mx = 0
dist = [[[-1]*m for _ in range(n)] for _ in range(h)]
q = deque()
for i in range(n):
    for j in range(m):
        for k in range(h):
            if board[k][i][j] == '1':
                dist[k][i][j] = 0
                q.append((k,i,j))
                rest -= 1
            elif board[k][i][j] == '-1':
                rest -= 1

def func():
    global rest, mx
    if rest == 0:
        print(0)
        return
    
    while q:
        z,x,y = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or ny < 0 or nz < 0 or nx >= n or ny >= m or nz >= h:
                continue
            if board[nz][nx][ny] != '0' or dist[nz][nx][ny] != -1:
                continue
            dist[nz][nx][ny] = dist[z][x][y] + 1
            q.append((nz,nx,ny))
            rest -= 1
            mx = max(mx, dist[nz][nx][ny])

    if rest:
        print(-1)
        return
    
    print(mx)

func()

'''
- #3차원_bfs
'''