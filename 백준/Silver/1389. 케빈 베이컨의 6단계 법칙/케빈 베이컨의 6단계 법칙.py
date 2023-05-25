import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[1e9]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = 0
mn = 1e9
for i in range(1, n+1):
    s = sum([x for x in graph[i] if x != 1e9])
    if s < mn:
        ans = i
        mn = s

print(ans)