### sys input ###

import sys

input = sys.stdin.readline

### solve ###

from collections import deque

N = int(input())
n = int(input())

graph = [[] for _ in range(N + 1)]  # 0 index는 사용 안함

for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

vis = [0] * (N + 1)
q = deque()

vis[1] = 1
q.append(1)

cnt = 0
while q:
    x = q.popleft()
    for nx in graph[x]:
        if vis[nx] != 0:
            continue
        vis[nx] = 1
        q.append(nx)
        cnt += 1

print(cnt)
