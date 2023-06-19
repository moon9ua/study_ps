from collections import deque

n, k = map(int, input().split())

q = deque()
vis = [-1] * 100005
cnt = [0] * 100005

q.append(n)
vis[n] = 0
cnt[n] = 1

while q:
    x = q.popleft()
    if x == k:
        continue
    for nx in (x-1, x+1, x*2):
        if nx < 0 or nx > 100000:
            continue
        if vis[nx] == -1:
            q.append(nx)
            vis[nx] = vis[x] + 1
            cnt[nx] = cnt[x]
        elif vis[nx] == vis[x] + 1:
            cnt[nx] += cnt[x]

print(vis[k])
print(cnt[k])