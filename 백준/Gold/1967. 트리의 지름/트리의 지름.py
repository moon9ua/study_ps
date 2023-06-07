from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def bfs(st):
    q = deque()
    dist = [-1] * (n+1)

    q.append(st)
    dist[st] = 0

    while q:
        x = q.popleft()
        for nx, nd in graph[x]:
            if dist[nx] != -1:
                continue
            q.append(nx)
            dist[nx] = dist[x] + nd

    idx = 0
    mx = 0
    for i in range(1, n+1):
        if mx < dist[i]:
            idx = i
            mx = dist[i]

    return (idx, mx)

v1, _ = bfs(1)
_, v2_dist = bfs(v1)
print(v2_dist)