from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
h = []
c = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            h.append((i,j))
        elif board[i][j] == 2:
            c.append((i,j))
            
ret = 1e9
for cb in combinations(c, m):
    tot_len = 0
    for (x1,y1) in h:    
        ch_len = 1e9
        for (x2,y2) in cb:
            ch_len = min(ch_len, abs(x1-x2) + abs(y1-y2))
        tot_len += ch_len
    ret = min(ret, tot_len)
    
print(ret)

'''
- #브루트_포스
- 백트래킹으로는 어떻게?
- 최적화 풀이 살펴보기
    - https://www.acmicpc.net/source/52857226
    - https://www.acmicpc.net/source/52855672
    - https://www.acmicpc.net/source/52859962
'''