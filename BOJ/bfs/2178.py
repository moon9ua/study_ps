from collections import deque
import sys
input = sys.stdin.readline
dx = [1,0,-1,0]
dy = [0,1,0,-1]

n,m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]

dist = [[-1] * m for _ in range(n)]
q = deque()
dist[0][0] = 1
q.append((0,0))

while q:
    x,y = q.popleft()
    if x == n-1 and y == m-1:
        print(dist[x][y])
        exit()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if board[nx][ny] == '0' or dist[nx][ny] != -1:
            continue
        dist[nx][ny] = dist[x][y] + 1
        q.append((nx,ny))