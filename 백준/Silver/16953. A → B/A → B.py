from collections import deque, defaultdict

a, b = map(int, input().split())

q = deque()
vis = defaultdict(lambda x: -1)

q.append(a)
vis[a] = 0

ans = 0
while q:
    x = q.popleft()
    if x == b:
        break
    for nx in (x*2, x*10 + 1):
        if nx > b:
            continue
        if nx in vis:
            continue
        q.append(nx)
        vis[nx] = vis[x] + 1

if not b in vis:
    print(-1)
else:
    print(vis[b] + 1)
