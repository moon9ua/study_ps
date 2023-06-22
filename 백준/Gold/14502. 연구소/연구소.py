from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline
dx = [1,0,-1,0]
dy = [0,1,0,-1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

empty = []
virus = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            empty.append((i,j))
        elif board[i][j] == 2:
            virus.append((i,j))

ans = -1e9
for cb in combinations(empty, 3):
    q = deque()
    vis = [[False] * m for _ in range(n)]

    for new_x, new_y in cb:
        vis[new_x][new_y] = True

    area = len(empty) - 3

    for vx,vy in virus:
        q.append((vx,vy))
        vis[vx][vy] = True
        while q:
            x,y = q.popleft()
            for a in range(4):
                nx = x + dx[a]
                ny = y + dy[a]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if board[nx][ny] != 0 or vis[nx][ny]:
                    continue
                q.append((nx,ny))
                vis[nx][ny] = True
                area -= 1

    ans = max(ans, area)

print(ans)