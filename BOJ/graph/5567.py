from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = defaultdict(list)
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

vis = [False] * (n+1)
q = deque()
ret = 0

vis[1] = True
q.append((1, 2))

while q:
    x,k = q.popleft()
    for nx in graph[x]:
        if vis[nx] == True:
            continue
        vis[nx] = True
        q.append((nx, k-1))
        if k-1 >= 0:
            ret += 1

print(ret)