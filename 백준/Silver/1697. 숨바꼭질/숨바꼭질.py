### sys input ###

import sys

input = sys.stdin.readline

### solve ###

from collections import deque

N, K = map(int, input().split())

vis = [-1] * 100004
q = deque()

vis[N] = 0
q.append(N)

while q:
    x = q.popleft()
    if x == K:
        break

    for nx in (x - 1, x + 1, 2 * x):
        if nx < 0 or nx > 100000:
            continue
        if vis[nx] != -1:
            continue
        vis[nx] = vis[x] + 1
        q.append(nx)

print(vis[K])
