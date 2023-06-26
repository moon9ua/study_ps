import sys
input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

r, c, t = map(int, input().split())
board = []
cond = []
for i in range(r):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(c):
        if board[i][j] == -1:
            cond.append((i, j))

def circulate(x, y, isup):
    curx, cury = x, y+1
    nval = 0

    while not (curx == x and cury == y):
        save = board[curx][cury]
        board[curx][cury] = nval
        nval = save
        if curx == x and 1 <= cury < c-1:
            cury += 1
        elif cury == c-1 and 1 <= curx < r-1:
            if isup:
                curx -= 1
            else:
                curx += 1
        elif (curx == 0 or curx == r-1) and cury != 0:
            cury -= 1
        else:
            if isup:
                curx += 1
            else:
                curx -= 1
        

for _ in range(t):
    d = [[0]*c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if board[x][y] <= 0:
                continue
            for a in range(4):
                nx = x + dx[a]
                ny = y + dy[a]
                if nx < 0 or ny < 0 or nx >= r or ny >= c:
                    continue
                if board[nx][ny] == -1:
                    continue
                d[nx][ny] += board[x][y] // 5
                d[x][y] -= board[x][y] // 5

    for i in range(r):
        for j in range(c):
            board[i][j] += d[i][j]

    circulate(*cond[0], True)
    circulate(*cond[1], False)

print(sum(map(sum, board)) + 2)