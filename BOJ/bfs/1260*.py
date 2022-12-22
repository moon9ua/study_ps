from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs
for g in graph:
    g.sort(reverse=True)

vis = [False] * (n+1)
st = []
ret = []

vis[v] = True
st.append(v)

while st:
    x = st.pop()
    if x in ret:
        continue
    ret.append(x)
    vis[x] = True
    for nx in graph[x]:
        if vis[nx] == True:
            continue
        st.append(nx)

print(*ret)

# bfs
for g in graph:
    g.sort()

vis = [False] * (n+1)
q = deque()
ret = []

vis[v] = True
q.append(v)

while q:
    x = q.popleft()
    ret.append(x)
    for nx in graph[x]:
        if vis[nx] == True:
            continue
        q.append(nx)
        vis[nx] = True

print(*ret)

'''
- 쉬워보이는데 까다롭다. "정점 번호가 작은 것을 먼저 방문"이 핵심
'''