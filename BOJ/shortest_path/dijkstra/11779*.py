import heapq
import sys
input = sys.stdin.readline
INF = 1e9

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,w = map(int, input().split())
    graph[u].append((v, w))
st, end = map(int, input().split())
dist = [INF] * (n+1)
pre = [0] * (n+1)

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
                pre[v] = now
    
func()

ret = [end]
curr = end
while curr != st:
    curr = pre[curr]
    ret.append(curr)

print(dist[end])
print(len(ret))
print(*ret[::-1])
