from collections import deque, defaultdict
import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
board = []
tot = 0
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)
    tot += row.count(1)

q = deque()
vis = [[False] * m for _ in range(n)]

q.append((0, 0))
vis[0][0] = True

cheeze = defaultdict(int)
cnt = 0

while tot:
    cnt += 1

    while q:
        x, y = q.popleft()
        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if vis[nx][ny]:
                continue
            if board[nx][ny] == 1:
                cheeze[(nx, ny)] += 1
            else:
                q.append((nx, ny))
                vis[nx][ny] = True

    for (x, y), v in list(cheeze.items()):
        if v >= 2:
            board[x][y] = 0
            tot -= 1
            del cheeze[(x, y)]
            q.append((x, y))
            vis[x][y] = True

print(cnt)