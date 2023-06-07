import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
st, ed = map(int, input().split())

pq = []
dist = [1e9] * (n+1)

heapq.heappush(pq, (0, st))
dist[st] = 0

while pq:
    d, x = heapq.heappop(pq)
    if dist[x] < d:
        continue
    for nx, nd in graph[x]:
        totd = d + nd
        if totd < dist[nx]:
            heapq.heappush(pq, (totd, nx))
            dist[nx] = totd

print(dist[ed])