import heapq
import sys
input = sys.stdin.readline
INF = 1e9

V,E = map(int, input().split())
st = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u].append((v, w))
dist = [INF] * (V+1)

def func():
    q = []
    dist[st] = 0
    heapq.heappush(q, (0, st))
    
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for v,w in graph[now]:
            cost = d + w
            if cost < dist[v]:
                dist[v] = cost
                heapq.heappush(q, (cost, v))
    
func()

for i in range(1, V+1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])
