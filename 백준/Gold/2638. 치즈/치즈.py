from collections import deque
import sys
input = sys.stdin.readline
dx = [1,0,-1,0]
dy = [0,1,0,-1]

n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            cnt += 1

def check(x, y, time):
    cnt = 0
    for a in range(4):
        nx = x + dx[a]
        ny = y + dy[a]
        if 0 <= vis[nx][ny] < time:
            cnt += 1
    return cnt >= 2

q = deque()
vis = [[-1] * m for _ in range(n)]

q.append((0,0))
vis[0][0] = 0
time = 0

while cnt:
    nxt = set()
    
    while q:
        x,y = q.popleft()
        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if vis[nx][ny] != -1:
                continue
            if board[nx][ny] == 0:
                q.append((nx,ny))
                vis[nx][ny] = time
            else:
                nxt.add((nx,ny))
    
    time += 1

    for x,y in nxt:
        if check(x, y, time):
            q.append((x,y))
            vis[x][y] = time
            board[x][y] = 0
            cnt -= 1

print(time)