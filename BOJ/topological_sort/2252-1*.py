from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = defaultdict(list)
ind = [0] * (n+1)
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    ind[b] += 1

q = deque(i for i in range(1,n+1) if not ind[i])
while q:
    x = q.popleft()
    print(x, end=' ')
    for nx in graph[x]:
        ind[nx] -= 1
        if not ind[nx]:
            q.append(nx)