from collections import deque
import sys
input = sys.stdin.readline
dx = [1,0,-1,0]
dy = [0,1,0,-1]

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

def func():
    q = deque()
    vis = [[False]*m for _ in range(n)]
    to_minus = [[0]*m for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] != 0 and not vis[i][j]:
                cnt += 1
                if cnt != 1:
                    return cnt
                q.append((i,j))
                vis[i][j] = True
                while q:
                    minus_cnt = 0
                    x,y = q.popleft()
                    for a in range(4):
                        nx = x + dx[a]
                        ny = y + dy[a]
                        if not 0<=nx<n or not 0<=ny<m:
                            continue
                        if board[nx][ny] == 0:
                            minus_cnt += 1
                            continue
                        if vis[nx][ny]:
                            continue
                        q.append((nx,ny))
                        vis[nx][ny] = True
                    to_minus[x][y] = minus_cnt

    for i in range(n):
        for j in range(m):
            if board[i][j] - to_minus[i][j] < 0:
                board[i][j] = 0
            else:
                board[i][j] -= to_minus[i][j]
                        
    return cnt

time = 0
while True:
    cnt = func()
    if cnt == 0:
        print(0)
        break
    elif cnt > 1:
        print(time)
        break
    time += 1