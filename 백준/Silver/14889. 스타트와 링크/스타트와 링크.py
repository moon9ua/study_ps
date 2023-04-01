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
        ans = min(ans, abs(calc_status(start)-calc_status(link)))
        return

    if len(start) < n//2:
        start.append(i)
        backtracking(i+1)
        start.pop()

    if len(link) < n//2:
        link.append(i)
        backtracking(i+1)
        link.pop()

def calc_status(team):
    status = 0
    for i,j in combinations(team, 2):
        status += mat[i][j]
        status += mat[j][i]
    return status

backtracking(0)
print(ans)