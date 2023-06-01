from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

up = [None] * 101
for _ in range(n):
    x,y = map(int, input().split())
    up[x] = y

down = [None] * 101
for _ in range(m):
    x,y = map(int, input().split())
    down[x] = y

q = deque()
vis = [-1] * 101
q.append(1)
vis[1] = 0

while q:
    x = q.popleft()

    for i in range(1, 7):
        nx = x + i

        if nx >= 100:
            print(vis[x]+1)
            exit()

        if up[nx]:
            nx = up[nx]
            while up[nx] or down[nx]:
                if up[nx]:
                    nx = up[nx]
                else:
                    nx = down[nx]
        elif down[nx]:
            nx = down[nx]
            while up[nx] or down[nx]:
                if up[nx]:
                    nx = up[nx]
                else:
                    nx = down[nx]

        if vis[nx] != -1:
            continue

        q.append(nx)
        vis[nx] = vis[x]+1