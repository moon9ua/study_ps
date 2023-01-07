from collections import defaultdict, deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)

n = int(input())
graph = defaultdict(list)
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

p = [0] * (n+1)
def dfs(x):
    for nx in graph[x]:
        if p[x] == nx:
            continue
        p[nx] = x
        dfs(nx)
dfs(1)

print(*p[2:], sep='\n')