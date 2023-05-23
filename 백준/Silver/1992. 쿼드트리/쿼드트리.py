import sys
input = sys.stdin.readline

n = int(input())
board = [input().rstrip() for _ in range(n)]

def pred(x, y, k):
    val = board[x][y]
    for i in range(k):
        for j in range(k):
            if val != board[x+i][y+j]:
                return False
    return True

def func(x, y, k):
    if k == 1:
        print(board[x][y], end='')
        return

    if pred(x, y, k):
        print(board[x][y], end='')
        return

    print('(', end='')
    d = k // 2
    for i in range(2):
        for j in range(2):
            nx = x + d*i
            ny = y + d*j
            func(nx, ny, d)
    print(')', end='')

func(0, 0, n)