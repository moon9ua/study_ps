from collections import deque
import sys

input = sys.stdin.readline
dx = [1,0,-1,0]
dy = [0,1,0,-1]

n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

ans = 0
while True:
    ans += 1

    nboard = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                tmp = 0
                for a in range(4):
                    ni = i + dx[a]
                    nj = j + dy[a]
                    if ni < 0 or nj < 0 or ni >= n or nj >= m:
                        continue
                    if board[ni][nj]:
                        continue
                    tmp += 1
                nboard[i][j] = max(0, board[i][j] - tmp)
    board = nboard

    cnt = 0
    vis = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not vis[i][j] and board[i][j]:
                vis[i][j] = True
                q = deque()
                q.append((i,j))
                cnt += 1
                while q:
                    x,y = q.popleft()
                    for a in range(4):
                        nx = x + dx[a]
                        ny = y + dy[a]
                        if nx < 0 or ny < 0 or nx >= n or ny >= m:
                            continue
                        if vis[nx][ny] or board[nx][ny] == 0:
                            continue
                        vis[nx][ny] = True
                        q.append((nx,ny))

    if cnt == 0:
        print(0)
        break
    elif cnt > 1:
        print(ans)
        break

'''
- Python3로 제출시 시간 초과, PyPy3로 제출시 통과
- 인덱스 중첩시 중복 유의: for a in range(4)
- 빙산 녹을 때 0이 최소: nboard[i][j] = max(0, board[i][j] - tmp)
'''