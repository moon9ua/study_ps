from collections import deque
import heapq
import sys
input = sys.stdin.readline

n,e = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1,v2 = map(int,input().split())

def find(st, ed):
    q = []
    dist = [1e9] * (n+1)
    heapq.heappush(q, (0,st))
    dist[st] = 0
    while q:
        d,x = heapq.heappop(q)
        if dist[x] < d:
            continue
        for nx,nd in graph[x]:
            totd = d + nd
            if totd < dist[nx]:
                heapq.heappush(q, (totd,nx))
                dist[nx] = totd
    return dist[ed]

between = find(v1,v2)
ret1 = find(1,v1) + between + find(v2,n)
ret2 = find(1,v2) + between + find(v1,n)
ret = min(ret1, ret2)

if ret >= 1e9:
    print(-1)
else:
    print(ret)