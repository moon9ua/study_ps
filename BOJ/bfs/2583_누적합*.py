import sys
from collections import deque

input = sys.stdin.readline
dx = [1,0,-1,0]
dy = [0,1,0,-1]

m, n, k = map(int, input().split())

pf = [[0] * (n+1) for _ in range(m+1)] # 유의: n+1, m+1
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    pf[y1][x1] += 1 # 고침: pf[x1][y1] = 1
    pf[y1][x2] -= 1
    pf[y2][x1] -= 1
    pf[y2][x2] += 1

vis = [[0] * (n+1) for _ in range(m+1)] # 유의: n+1, m+1
for i in range(1, m+1):
    for j in range(1, n+1):
        vis[i][j] = pf[i-1][j-1] + vis[i-1][j] + vis[i][j-1] - vis[i-1][j-1] # 누적합 식

cnt = 0
rets = []
for i in range(m):
    for j in range(n):
        if vis[i+1][j+1] == 0:
            cnt += 1
            ret = 1
            q = deque()
            q.append((i, j))
            vis[i+1][j+1] = 1
            while q:
                x, y = q.pop()
                for a in range(4):
                    nx = x + dx[a]
                    ny = y + dy[a]
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        continue
                    if vis[nx+1][ny+1] != 0:
                        continue
                    q.append((nx, ny))
                    vis[nx+1][ny+1] = 1
                    ret += 1
            rets.append(ret)
            
print(cnt)
print(*sorted(rets))

'''
- 배열 시각화: pprint 모듈
- 구간합
- 2차원 배열 (y,x) 좌표 입력
'''