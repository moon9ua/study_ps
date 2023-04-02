from collections import deque
import sys
input = sys.stdin.readline
dx = [1,0,-1,0]
dy = [0,1,0,-1]

n = int(input())
board = []
mn = 1e9
mx = -1e9
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)
    mn = min(mn, min(row))
    mx = max(mx, max(row))

ans = 1
def find(rain):
    global ans
    vis = [[False]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not vis[i][j] and board[i][j] > rain:
                q = deque()
                vis[i][j] = True
                q.append((i,j))
                cnt += 1
                while q:
                    x,y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        if vis[nx][ny] or board[nx][ny] <= rain:
                            continue
                        vis[nx][ny] = True
                        q.append((nx,ny))

    ans = max(ans, cnt)

for i in range(mn, mx):
    find(i)

print(ans)
