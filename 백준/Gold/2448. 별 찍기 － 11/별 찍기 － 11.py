import math

n = int(input())
k = int(math.log2(n // 3))

r, c = n, 6 * n // 3 - 1

board = [[' ']*c for _ in range(r)]

def draw(x, y, k):
    if k == 0:
        board[x][y] = '*'
        board[x+1][y-1] = '*'
        board[x+1][y+1] = '*'
        for i in range(5):
            board[x+2][y-2+i] = '*'
        return

    dx = 3 * 2**(k-1)
    dy = 3 * 2**(k-1)
    draw(x, y, k-1)
    draw(x+dx, y-dy, k-1)
    draw(x+dx, y+dy, k-1)

draw(0, c//2, k)

print(*[''.join(row) for row in board], sep='\n')
