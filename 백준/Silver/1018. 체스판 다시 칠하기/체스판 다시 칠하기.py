n,m = map(int, input().split())
board = [input() for _ in range(n)]

ret = 1e9

for x in range(0, n-7):
    for y in range(0, m-7):
        to_paint_w = 0
        to_paint_b = 0
        
        for i in range(0, 8):
            for j in range(0, 8):
                nx = i+x
                ny = j+y
                if (nx+ny)%2 == 0 and board[nx][ny] != 'W':
                    to_paint_w += 1
                elif (nx+ny)%2 == 1 and board[nx][ny] != 'B':
                    to_paint_w += 1

                if (nx+ny)%2 == 0 and board[nx][ny] != 'B':
                    to_paint_b +=1
                elif (nx+ny)%2 == 1 and board[nx][ny] != 'W':
                    to_paint_b += 1
        
        ret = min(ret, to_paint_b, to_paint_w)

print(ret)