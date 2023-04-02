from collections import deque
import sys

input = sys.stdin.readline
dx = [1,0,-1,0]
dy = [0,1,0,-1]

r,c = map(int, input().split())
board = [input().rstrip() for _ in range(r)]

vis = [[False]*c for _ in range(r)]
used = [False] * 200
mx = 1

def func(x,y,k):
    global mx
    
    for a in range(4):
        nx = x + dx[a]
        ny = y + dy[a]
        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue
        if vis[nx][ny] or used[ord(board[nx][ny])]:
            continue
        vis[nx][ny] = True
        used[ord(board[nx][ny])] = True
        mx = max(mx, k+1)
        func(nx,ny,k+1)
        vis[nx][ny] = False
        used[ord(board[nx][ny])] = False

vis[0][0] = True
used[ord(board[0][0])] = True
func(0,0,1)

print(mx)