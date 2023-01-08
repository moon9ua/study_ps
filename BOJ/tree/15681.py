from collections import deque, defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)

N,R,Q = map(int, input().split())
graph = defaultdict(list)
for _ in range(N-1):
    U,V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

p = [0] * (N+1)
size = [0] * (N+1)

def dfs(node):
    size[node] += 1
    for nx in graph[node]:
        if p[node] == nx:
            continue
        p[nx] = node
        dfs(nx)
        size[node] += size[nx]

dfs(R)

for _ in range(Q):
    a = int(input())
    print(size[a])

'''
- setrecursionlimit 항상 주의
- 서브트리 정점 수 구하는 법
'''