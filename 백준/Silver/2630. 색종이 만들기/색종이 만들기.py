import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0

def valid(x, y, k):
    color = board[x][y]
    for i in range(x, x+k):
        for j in range(y, y+k):
            if board[i][j] != color:
                return False
    return True

def func(x, y, k):
    global white, blue

    if k == 1:
        if board[x][y] == 1:
            blue += 1
        else:
            white += 1
        return

    if valid(x, y, k):
        if board[x][y] == 1:
            blue += 1
        else:
            white += 1
        return

    half = k // 2
    func(x, y, half)
    func(x+half, y, half)
    func(x, y+half, half)
    func(x+half, y+half, half)

func(0, 0, n)

print(white)
print(blue)