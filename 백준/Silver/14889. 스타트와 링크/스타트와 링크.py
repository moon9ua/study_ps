from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]

mn = 1e9
for c in combinations(range(n), n//2):
    start = set(c)
    link = set(range(n)) - start
    tot_s = 0
    tot_l = 0
    for x,y in combinations(start, 2):
        tot_s += mat[x][y]
        tot_s += mat[y][x]
    for x,y in combinations(link, 2):
        tot_l += mat[x][y]
        tot_l += mat[y][x]
    mn = min(mn, abs(tot_s - tot_l))

print(mn)