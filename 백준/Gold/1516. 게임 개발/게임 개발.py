from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
ind = [0] * (n+1)
time = [0] * (n+1)
for i in range(1,n+1):
    a, *blist, c = map(int, input().split())
    time[i] = a
    for b in blist:
        graph[b].append(i)
        ind[i] += 1

q = deque()
ret = [0] * (n+1)
for i in range(1,n+1):
    if ind[i] == 0:
        q.append(i)
        ret[i] = time[i]

while q:
    x = q.popleft()
    for nx in graph[x]:
        ind[nx] -= 1
        ret[nx] = max(ret[nx], ret[x]+time[nx])
        if ind[nx] == 0:
            q.append(nx)

print(*ret[1:], sep='\n')