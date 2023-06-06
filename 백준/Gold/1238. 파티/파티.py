import heapq
import sys
input = sys.stdin.readline

n, m, X = map(int, input().split())
graph = [[] for _ in range(n+1)]
rev_graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    rev_graph[b].append((a, t))

def daik(a, g):
    pq = []
    dist = [1e9] * (n+1)

    heapq.heappush(pq, (0, a))
    dist[a] = 0

    while pq:
        d, x = heapq.heappop(pq)
        if dist[x] < d:
            continue
        for nx, nd in g[x]:
            totd = d + nd
            if totd < dist[nx]:
                dist[nx] = totd
                heapq.heappush(pq, (totd, nx))

    return dist

from_x = daik(X, graph)
to_x = daik(X, rev_graph)

mx = 0
for i in range(1, n+1):
    dist = from_x[i] + to_x[i]
    mx = max(mx, dist)

print(mx)