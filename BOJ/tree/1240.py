from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1111)

n,m = map(int, input().split())
graph = defaultdict(list)
for _ in range(n-1):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dfs(a,b,d):
    if a == b:
        print(d)
        return
    for nx,cost in graph[a]:
        if p[a] == nx:
            continue
        p[nx] = a
        dfs(nx,b,d+cost)

for _ in range(m):
    a,b = map(int, input().split())
    p = [0] * (n+1)
    dfs(a,b,0)