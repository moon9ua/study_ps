from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = defaultdict(list)
deg = [0] * (n+1)
for _ in range(m):
    a,b = map(int, input().split())
    graph[b].append(a)
    deg[a] += 1

q = deque(i for i in range(1, n+1) if deg[i] == 0)
ret = []
while q:
    x = q.popleft()
    ret.append(x)
    for nx in graph[x]:
        deg[nx] -= 1
        if deg[nx] == 0:
            q.append(nx)

print(*ret[::-1])
