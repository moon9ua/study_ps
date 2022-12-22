from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
t = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(t):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
vis = [0] * (n+1)
q = deque()
vis[1] = 1
q.append(1)

ret = 0
while q:
    x = q.popleft()
    ret += 1
    for nx in graph[x]:
        if vis[nx] != 0:
            continue
        vis[nx] = 1
        q.append(nx)
    
print(ret - 1)