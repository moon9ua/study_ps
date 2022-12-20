from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

s = set(range(n))
ret = 1e9

for c in combinations(range(n), n//2):
    start = 0
    link = 0
    
    for (i,j) in combinations(c, 2):
        start += arr[i][j]
        start += arr[j][i]
    
    for (i,j) in combinations(s-set(c), 2):
        link += arr[i][j]
        link += arr[j][i]
        
    ret = min(ret, abs(start-link))

print(ret)

'''
- 훨씬 최적화된 코드의 풀이를 보려면 https://www.acmicpc.net/board/view/72643
'''