import sys
from collections import deque

input = sys.stdin.readline
dx = [1,0,-1,0]
dy = [0,1,0,-1]

m, n, k = map(int, input().split())
vis = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2): # 헷갈: range 범위
        for y in range(y1, y2):
            vis[y][x] = 1 # 고침: vis[x][y] = 1

cnt = 0
rets = []
for i in range(m):
    for j in range(n):
        if vis[i][j] == 0:
            cnt += 1
            ret = 1 # 고침: ret = 0
            q = deque()
            q.append((i, j))
            vis[i][j] = 1
            while q:
                x, y = q.pop()
                for a in range(4):
                    nx = x + dx[a]
                    ny = y + dy[a]
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        continue
                    if vis[nx][ny] == 1:
                        continue
                    q.append((nx, ny))
                    vis[nx][ny] = 1
                    ret += 1
            rets.append(ret)
            
print(cnt)
print(*sorted(rets))