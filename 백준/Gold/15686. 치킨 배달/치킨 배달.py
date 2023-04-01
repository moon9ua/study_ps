from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
home = []
ch = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            home.append((i,j))
        elif board[i][j] == 2:
            ch.append((i,j))
            
ret = 1e9
for cb in combinations(ch, m):
    tot_len = 0
    for (x1,y1) in home:    
        ch_len = 1e9
        for (x2,y2) in cb:
            ch_len = min(ch_len, abs(x1-x2) + abs(y1-y2))
        tot_len += ch_len
    ret = min(ret, tot_len)
    
print(ret)