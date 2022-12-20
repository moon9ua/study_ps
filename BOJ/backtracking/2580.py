import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]
to_fill = [(i,j) for i in range(9) for j in range(9) if board[i][j] == 0]

def can_fill(x, y):
    nums = [i for i in range(1, 10)]

    for i in range(9):
        if board[x][i] in nums:
            nums.remove(board[x][i])
            continue
        if board[i][y] in nums:
            nums.remove(board[i][y])

    nx = x//3 * 3
    ny = y//3 * 3
    for i in range(3):
        for j in range(3):
            if board[nx+i][ny+j] in nums:
                nums.remove(board[nx+i][ny+j])

    return nums

def func(k):
    if k == len(to_fill):
        for i in range(9):
            print(*board[i])
        exit()
        
    x, y = to_fill[k]
    for i in can_fill(x, y):
        board[x][y] = i
        func(k+1)
        board[x][y] = 0

func(0)

'''
- #백트래킹

- board[x][y] = 0 을 안하면, can_fill이 제대로 동작하지 않는다.
- 틀렸던 답안 확인할 것... can_fill 개선해야 통과헸음.
'''