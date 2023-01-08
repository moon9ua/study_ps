from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n = int(input())
graph = defaultdict(list)
while True:
    a,b = map(int, input().split())
    if a == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

def bfs(x):
    dist = [-1] * (n+1)
    q = deque()
    dist[x] = 0
    q.append(x)

    while q:
        x = q.popleft()
        for nx in graph[x]:
            if dist[nx] != -1:
                continue
            dist[nx] = dist[x] + 1
            q.append(nx)

    return max(dist)

ret = []
for i in range(1, n+1):
    ret.append(bfs(i))

print(min(ret), ret.count(min(ret)))
print(*[i+1 for i in range(n) if ret[i] == min(ret)])
