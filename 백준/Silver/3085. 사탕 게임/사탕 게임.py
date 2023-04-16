import sys
input = sys.stdin.readline
dx = [1,0,-1,0]
dy = [0,1,0,-1]

n = int(input())
board = [input().rstrip() for _ in range(n)]

def search():
    ret = 0
    for i in range(n):
        lenX, lenY = 1,1
        for j in range(1, n):
            if tmp[i][j-1] == tmp[i][j]:
                lenX += 1
                ret = max(ret, lenX)
            else:
                lenX = 1

            if tmp[j-1][i] == tmp[j][i]:
                lenY += 1
                ret = max(ret, lenY)
            else:
                lenY = 1
    return ret

cnt = 0
tmp = [list(row) for row in board]
for i in range(n):
    for j in range(n):
        if i < n-1 and tmp[i][j] != tmp[i+1][j]:
            tmp[i][j], tmp[i+1][j] = tmp[i+1][j], tmp[i][j]
            cnt = max(cnt, search())
            tmp[i][j], tmp[i+1][j] = tmp[i+1][j], tmp[i][j] 

        if j < n-1 and tmp[i][j] != tmp[i][j+1]:
            tmp[i][j], tmp[i][j+1] = tmp[i][j+1], tmp[i][j]
            cnt = max(cnt, search())
            tmp[i][j], tmp[i][j+1] = tmp[i][j+1], tmp[i][j]

print(cnt)