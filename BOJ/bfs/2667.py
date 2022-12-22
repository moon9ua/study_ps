from collections import deque
import sys
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]

n = int(input())
board = [input().rstrip() for _ in range(n)]
vis = [[False] * n for _ in range(n)]

def bfs(i,j):
    q = deque()
    vis[i][j] = True
    q.append((i,j))
    area = 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if vis[nx][ny] == True or board[nx][ny] == '0':
                continue
            vis[nx][ny] = True
            q.append((nx,ny))
            area += 1

    return area

cnt = 0
ret = []
for i in range(n):
    for j in range(n):
        if board[i][j] == '1' and vis[i][j] == False:
            cnt += 1
            ret.append(bfs(i,j))

print(cnt)
print(*sorted(ret), sep='\n')