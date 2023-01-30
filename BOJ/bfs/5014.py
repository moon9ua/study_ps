from collections import deque
import sys
input = sys.stdin.readline

f,s,g,u,d = map(int, input().split())
dx = [u,-d]

vis = [-1] * (f+1)
q = deque()
vis[s] = 0
q.append(s)

while q:
    x = q.popleft()
    if x == g:
        break
    for d in dx:
        nx = x + d
        if nx < 1 or nx > f:
            continue
        if vis[nx] != -1:
            continue
        vis[nx] = vis[x]+1
        q.append(nx)

if vis[g] == -1:
    print('use the stairs')
else:
    print(vis[g])

'''
- vis 배열 -1 초기화
'''