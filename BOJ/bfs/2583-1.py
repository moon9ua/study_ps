from collections import deque
import sys
input = sys.stdin.readline
dx = [1,0,-1,0]
dy = [0,1,0,-1]

m,n,k = map(int, input().split())
board = [[1]*m for _ in range(n)]

for _ in range(k):
    x1,y1,x2,y2 = map(int, input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            board[i][j] = 0

vis = [[False]*m for _ in range(n)]
q = deque()

def bfs(i,j):
    vis[i][j] = True
    q.append((i,j))
    area = 0

    while q:
        x,y = q.popleft()
        area += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if board[nx][ny] == 0 or vis[nx][ny] == True:
                continue
            vis[nx][ny] = True
            q.append((nx,ny))

    return area

cnt = 0
areas = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and vis[i][j] == False:
            cnt += 1
            areas.append(bfs(i,j))

print(cnt)
print(*sorted(areas))

'''
- 누적합으로도 가능할 것 같으나, nmk가 모두 100 이하라 누적합을 안해도 괜찮은 듯
'''