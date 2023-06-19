from collections import deque

n, k = map(int, input().split())

if n == k:
    print(0)
    print(1)
    exit()

q = deque()
vis = [-1] * 200005

q.append(n)
vis[n] = 0

ans = 0
cnt = 0
while q:
    x = q.popleft()
    for nx in (x-1, x+1, x*2):
        if nx < 0 or nx > 200000:
            continue
        if nx == k:
            if vis[nx] == -1:
                vis[nx] = vis[x] + 1
                cnt += 1
            elif vis[nx] == vis[x] + 1:
                cnt += 1
        else:
            if vis[nx] != -1 and vis[nx] != vis[x] + 1:
                continue
            q.append(nx)
            vis[nx] = vis[x] + 1

print(vis[k])
print(cnt)