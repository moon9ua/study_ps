### sys input ###

import sys

input = sys.stdin.readline

### solve ###

from collections import deque


def bfs(i, j, board, row, col):
    if board[i][j] == 0:
        return False

    q = deque()

    board[i][j] = 0
    q.append((i, j))

    while q:
        x, y = q.popleft()

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= row or ny >= col:
                continue
            if board[nx][ny] == 0:
                continue

            board[nx][ny] = 0
            q.append((nx, ny))

    return True


def sol():
    row, col, k = map(int, input().split())
    board = [[0] * col for _ in range(row)]

    for _ in range(k):
        x, y = map(int, input().split())
        board[x][y] = 1

    cnt = 0
    for i in range(row):
        for j in range(col):
            cnt += bfs(i, j, board, row, col)

    print(cnt)


t = int(input())

for _ in range(t):
    sol()
