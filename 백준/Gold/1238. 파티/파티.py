import heapq
import sys
input = sys.stdin.readline

n, m, X = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))

# a부터 모든 정점까지의 최단 거리
def daik(a):
    pq = []
    dist = [1e9] * (n+1)

    heapq.heappush(pq, (0, a))
    dist[a] = 0

    while pq:
        d, x = heapq.heappop(pq)
        if dist[x] < d:
            continue
        for nx, nd in graph[x]:
            totd = d + nd
            if totd < dist[nx]:
                dist[nx] = totd
                heapq.heappush(pq, (totd, nx))

    return dist

from_x = daik(X)

ans = 0
for i in range(1, n+1):
    tmp = from_x[i] + daik(i)[X]
    ans = max(ans, tmp)

print(ans)