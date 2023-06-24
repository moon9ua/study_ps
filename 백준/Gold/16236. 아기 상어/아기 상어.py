from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
board = []
food = [0] * 10
cur = None
for i in range(n):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(n):
        if board[i][j] == 9:
            cur = (i, j)
            board[i][j] = 0
        elif board[i][j] != 0:
            food[board[i][j]] += 1

time = 0
size = 2
rest = size
d = ((-1,0), (0,-1), (0,1), (1,0))
while sum(food[:size]):
    q = deque()
    vis = [[-1]*n for _ in range(n)]

    q.append(cur)
    vis[cur[0]][cur[1]] = 0

    nxt_d = 1e9
    nxt_lst = []
    while q:
        x, y = q.popleft()
        if board[x][y] and board[x][y] < size:
            if nxt_d == 1e9:
                nxt_d = vis[x][y]
                nxt_lst.append((x, y))
            elif nxt_d == vis[x][y]:
                nxt_lst.append((x, y))
            continue
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if board[nx][ny] > size or vis[nx][ny] != -1:
                continue
            q.append((nx, ny))
            vis[nx][ny] = vis[x][y] + 1

    if not nxt_lst:
        break

    nx, ny = max(nxt_lst, key=lambda x: (-x[0], -x[1]))
    rest -= 1
    if rest == 0:
        size += 1
        rest = size
    food[board[nx][ny]] -= 1
    time += vis[nx][ny]
    cur = (nx, ny)
    board[nx][ny] = 0
        
print(time)
