import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline

v,e = map(int,input().split())
st = int(input())
graph = defaultdict(list)
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
dist = [1e9] * (v+1)

q = []
dist[st] = 0
heapq.heappush(q, (0, st))
while q:
    d, x = heapq.heappop(q)
    if dist[x] < d:
        continue
    for nx, nd in graph[x]:
        totd = d + nd
        if totd < dist[nx]:
            dist[nx] = totd
            heapq.heappush(q, (totd, nx))

for i in range(1, v+1):
    if dist[i] == 1e9:
        print('INF')
    else:
        print(dist[i])