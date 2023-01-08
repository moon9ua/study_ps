from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n = int(input())
graph = defaultdict(list)
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            graph[i].append(j)

def bfs(i, j):
    vis = [False] * n
    q = deque()
    vis[i] = True
    q.append(i)

    while q:
        x = q.popleft()
        for nx in graph[x]:
            if nx == j:
                return True
            if vis[nx]:
                continue
            vis[nx] = True
            q.append(nx)

    return False

for i in range(n):
    for j in range(n):
        print(int(bfs(i,j)), end=' ')
    print()
