from collections import deque

n, k = map(int, input().split())

q = deque()
vis = [-1] * 100005

q.append(n)
vis[n] = 0

ans = 0
cnt = 0
while q:
    x = q.popleft()
    if x == k:
        cnt += 1
        continue
    for nx in (x-1, x+1, x*2):
        if nx < 0 or nx > 100000:
            continue
        if vis[nx] != -1 and vis[nx] != vis[x] + 1:
            continue
        q.append(nx)
        vis[nx] = vis[x] + 1

print(vis[k])
print(cnt)