from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]

ans = 1e9
start = []
link = []

def backtracking(i):
    global ans

    if i == n:
        ans = min(ans, calc())
        return

    if len(start) < n//2:
        start.append(i)
        backtracking(i+1)
        start.pop()

    if len(link) < n//2:
        link.append(i)
        backtracking(i+1)
        link.pop()

def calc():
    tot_s = 0
    tot_l = 0
    for i,j in combinations(start, 2):
        tot_s += mat[i][j]
        tot_s += mat[j][i]
    for i,j in combinations(link, 2):
        tot_l += mat[i][j]
        tot_l += mat[j][i]
    return abs(tot_s - tot_l)

backtracking(0)
print(ans)