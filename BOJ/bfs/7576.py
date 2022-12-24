from collections import deque
import sys
input = sys.stdin.readline
dx = [1,0,-1,0]
dy = [0,1,0,-1]

m,n = map(int, input().split())
board = [input().rstrip().split() for _ in range(n)]

rest = m*n
mx = 0
dist = [[-1]*m for _ in range(n)]
q = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == '1':
            dist[i][j] = 0
            q.append((i,j))
            rest -= 1
        elif board[i][j] == '-1':
            rest -= 1

def func():
    global rest, mx
    
    if rest == 0:
        print(0)
        return
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if board[nx][ny] != '0' or dist[nx][ny] != -1:
                continue
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx,ny))
            rest -= 1
            mx = max(mx, dist[nx][ny])

    if rest:
        print(-1)
        return
    
    print(mx)

func()

'''
- ? 객체가 아닌 전역변수는 함수내에서 사용하려면 global 키워드 붙여야... (배열, deque 등은 그냥 사용 가능)
'''