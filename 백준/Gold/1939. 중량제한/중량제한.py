from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = defaultdict(list)

mx = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    mx = max(mx, c)

a, b = map(int, input().split())

def check(mid):
    q = deque()
    vis = [False] * (n+1)
    q.append(a)
    vis[a] = True
    while q:
        x = q.popleft()
        for nx,nc in graph[x]:
            if vis[nx]:
                continue
            if nc < mid:
                continue
            if nx == b:
                return True
            q.append(nx)
            vis[nx] = True
    return False

l, r = 0, mx+1
while l+1 < r:
    mid = (l+r) // 2
    if check(mid):
        l = mid
    else:
        r = mid

print(l)