from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n,m,v = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n+1):
    # graph[i] = sorted(list(set(graph[i]))) # 어짜피 vis로 관리하므로, 중복 제거 필요가 없다. (시간복잡도 차이는?)
    graph[i].sort()

vis = [False] * (n+1)
def dfs(x):
    vis[x] = True
    print(x, end=' ')
    for nx in graph[x]:
        if vis[nx]:
            continue
        dfs(nx)

def bfs():
    vis = [False] * (n+1)
    q = deque()
    vis[v] = True
    q.append(v)
    
    ret = [v]
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if vis[nx]:
                continue
            vis[nx] = True
            q.append(nx)
            ret.append(nx)

    print(*ret)

dfs(v)
print()
bfs()