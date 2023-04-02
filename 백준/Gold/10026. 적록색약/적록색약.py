from collections import deque
import sys
input = sys.stdin.readline
dx = [1,0,-1,0]
dy = [0,1,0,-1]

nm = {'R':1, 'G':2, 'B':3}
ab = {'R':1, 'G':1, 'B':3}

n = int(input())
board = [input().rstrip() for _ in range(n)]
vis_nm = [[False]*n for _ in range(n)]
vis_ab = [[False]*n for _ in range(n)]

cnt_nm = 0
for i in range(n):
    for j in range(n):
        if vis_nm[i][j]:
            continue
        cnt_nm += 1
        q = deque()
        q.append((i,j))
        vis_nm[i][j] = True
        while q:
            x,y = q.popleft()
            for a in range(4):
                nx = x + dx[a]
                ny = y + dy[a]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if nm[board[nx][ny]] != nm[board[x][y]] or vis_nm[nx][ny]:
                    continue
                q.append((nx,ny))
                vis_nm[nx][ny] = True

cnt_ab = 0
for i in range(n):
    for j in range(n):
        if vis_ab[i][j]:
            continue
        cnt_ab += 1
        q = deque()
        q.append((i,j))
        vis_ab[i][j] = True
        while q:
            x,y = q.popleft()
            for a in range(4):
                nx = x + dx[a]
                ny = y + dy[a]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if ab[board[nx][ny]] != ab[board[x][y]] or vis_ab[nx][ny]:
                    continue
                q.append((nx,ny))
                vis_ab[nx][ny] = True

print(cnt_nm, cnt_ab)