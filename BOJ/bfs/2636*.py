from collections import deque
import sys
input = sys.stdin.readline
dx = [1,0,-1,0]
dy = [0,1,0,-1]

n,m = map(int, input().split())
board = [list(input().rstrip().split()) for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == '1':
            cnt += 1

def bfs():
    global cnt, todo
    vis = [[False]*m for _ in range(n)]
    q = deque(todo)
    todo = []

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if vis[nx][ny]:
                continue
            if board[nx][ny] == '1':
                vis[nx][ny] = True
                todo.append((nx,ny))
                board[nx][ny] = '0'
                cnt -= 1
            else:
                vis[nx][ny] = True
                q.append((nx,ny))

time = 0
history = [0]
todo = [(0,0)]

while cnt:
    time += 1
    history.append(cnt)
    bfs()

print(time)
print(history[-1])

'''
- 더 깔끔한 방법이 없을까?
'''