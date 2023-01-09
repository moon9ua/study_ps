from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = defaultdict(list)
ind = [0] * (n+1)
for _ in range(m):
    cnt, *order = map(int, input().split())
    for i in range(cnt-1):
        graph[order[i]].append(order[i+1])
        ind[order[i+1]] += 1

q = deque(i for i in range(1, n+1) if not ind[i])
ret = []
while q:
    x = q.popleft()
    ret.append(x)
    for nx in graph[x]:
        ind[nx] -= 1
        if not ind[nx]:
            q.append(nx)

if len(ret) != n:
    print(0)
else:
    print(*ret, end='\n')