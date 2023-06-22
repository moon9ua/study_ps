# combination 사용하지 않고 재귀로 최적화 시도

from collections import deque
import sys
input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

empty = []
virus = []
area = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            empty.append((i, j))
            area += 1
        elif board[i][j] == 2:
            virus.append((i, j))
area -= 3

def bfs():
    q = deque(virus)
    vis = [[False]*m for _ in range(n)]
    cnt = area

    for x, y in virus:
        vis[x][y] = True

    while q:
        x, y = q.popleft()
        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if board[nx][ny] != 0 or vis[nx][ny]:
                continue
            q.append((nx, ny))
            vis[nx][ny] = True
            cnt -= 1

    return cnt

mx = 0
used = [False] * 100
def func(st, k):
    global mx

    if k == 3:
        mx = max(mx, bfs())
        return

    for i in range(st, len(empty)):
        if not used[i]:
            x, y = empty[i]
            used[i] = True
            board[x][y] = 1
            func(i, k+1)
            used[i] = False
            board[x][y] = 0
        
func(0, 0)
print(mx)