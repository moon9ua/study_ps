from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1111)

n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(x):
    for nx in graph[x]:
        if vis[nx]:
            continue
        vis[nx] = True
        dfs(nx)

cnt = 0
vis = [False] * (n+1)

for i in range(1, n+1):
    if not vis[i]:
        cnt += 1
        dfs(i)

print(cnt)