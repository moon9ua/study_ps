from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n = int(input())
graph = defaultdict(list)
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

p = [0] * (n+1)
q = deque()
q.append(1)
while q:
    x = q.popleft()
    for nx in graph[x]:
        if p[x] == nx:
            continue
        q.append(nx)
        p[nx] = x

print(*p[2:], sep='\n')