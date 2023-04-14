import heapq
import sys
input = sys.stdin.readline

v,e = map(int,input().split())
st = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

dist = [1e9] * (v+1)
pq = []

dist[st] = 0
heapq.heappush(pq, (0,st))

while pq:
    d,x = heapq.heappop(pq)
    if dist[x] < d:
        continue
    for nx,nd in graph[x]:
        totd = d + nd
        if totd < dist[nx]:
            dist[nx] = totd
            heapq.heappush(pq, (totd,nx))

ret = ['INF' if d==1e9 else d for d in dist]
print(*ret[1:], sep='\n')