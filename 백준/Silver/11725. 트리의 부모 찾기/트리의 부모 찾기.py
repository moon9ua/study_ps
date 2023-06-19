import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

p = [None] * (n+1)

def func(x):
    for nx in graph[x]:
        if p[nx]:
            continue
        p[nx] = x
        func(nx)

p[1] = 0
func(1)

print(*p[2:], sep='\n')