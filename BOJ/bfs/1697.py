from collections import deque

n,k = map(int, input().split())
dist = [1e9] * 100002

q = deque()
dist[n] = 0
q.append(n)

while q:
    x = q.popleft()
    if x == k:
        print(dist[x])
        exit()
    for nx in [x-1, x+1, x*2]:
        if nx < 0 or nx > 100000:
            continue
        if dist[x] + 1 >= dist[nx]:
            continue
        dist[nx] = dist[x] + 1
        q.append(nx)
