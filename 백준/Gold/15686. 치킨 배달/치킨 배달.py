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

rets = []
c = []
def func(k):
    if len(c) == m:
        tot = 0
        for x1,y1 in home:
            dist = 1e9
            for x2,y2 in c:
                dist = min(dist, abs(x1-x2)+abs(y1-y2))
            tot += dist
        rets.append(tot)
        return

    if k == len(ch):
        return

    c.append(ch[k])
    func(k+1)
    c.pop()
    func(k+1)

func(0)
print(min(rets))