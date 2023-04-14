from collections import deque
import sys
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]

n,m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]

def bfs():
    vis = [[[-1]*2 for _ in range(m)] for _ in range(n)]
    q = deque()

    vis[0][0][0] = 1
    q.append((0,0,0))

    while q:
        x,y,k = q.popleft()
        if x == n-1 and y == m-1:
            return vis[x][y][k]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if board[nx][ny] == '1' and not k:
                vis[nx][ny][1] = vis[x][y][0] + 1
                q.append((nx,ny,1))
            if board[nx][ny] == '0' and vis[nx][ny][k] == -1:
                vis[nx][ny][k] = vis[x][y][k] + 1
                q.append((nx,ny,k))
    
    return -1

print(bfs())