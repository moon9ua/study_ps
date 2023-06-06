import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
dist = [1e9] * (N+1)

dist[1] = 0
neg_cycle = False
for i in range(N):
    for j in range(M):
        cur, nxt, cost = edges[j]
        if dist[cur] != 1e9 and dist[nxt] > dist[cur] + cost:
            dist[nxt] = dist[cur] + cost
            if i == N-1:
                neg_cycle = True # 음수 사이클 존재

if neg_cycle:
    print(-1)
else:
    print(*[d if d != 1e9 else -1 for d in dist[2:]], sep='\n')