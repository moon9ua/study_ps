from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

vis = [False] * (n+1)
q = deque()
ret = 0
for i in range(1, n+1):
    if vis[i] == True:
        continue
    vis[i] = True
    q.append(i)
    ret += 1
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if vis[nx] == True:
                continue
            vis[nx] = True
            q.append(nx)

print(ret)

'''
- 그래프 인접리스트 defaultdict
'''