from collections import deque
import sys

input = sys.stdin.readline

n,k = map(int,input().split())
dist = [-1] * 100005

dist[n] = 0
q = deque()
q.append(n)

while q:
    x = q.popleft()
    if x == k:
        break

    nx = x*2
    if 0 <= nx <= 100000 and dist[nx] == -1:
        dist[nx] = dist[x]
        q.appendleft(nx)

    for nx in [x-1,x+1]:
        if nx < 0 or nx > 100000:
            continue
        if dist[nx] != -1:
            continue
        dist[nx] = dist[x]+1
        q.append(nx)

print(dist[k])

'''
- 0-1 bfs
- https://www.acmicpc.net/board/view/38887#comment-69010
'''