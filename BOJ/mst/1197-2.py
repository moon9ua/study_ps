from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

v,e = map(int, input().split())
graph = defaultdict(list)
for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

vis = [False] * (v+1)
pq = []
vis[1] = True
for c,x in graph[1]:
    heapq.heappush(pq, (c,1,x))

ret = 0
cnt = 0
while pq:
    c,a,b = heapq.heappop(pq)
    if vis[b]:
        continue
    vis[b] = True
    ret += c
    cnt += 1
    for nc,nx in graph[b]:
        if not vis[nx]:
            heapq.heappush(pq, (nc,b,nx))

print(ret)