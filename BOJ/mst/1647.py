import sys
input = sys.stdin.readline

n,m = map(int, input().split())
edges = []
for _ in range(m):
    a,b,c = map(int, input().split())
    edges.append((c,a,b))
edges.sort()

p = list(range(n+1))

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(a, b):
    x = find(a)
    y = find(b)
    if x < y:
        p[y] = x
    else:
        p[x] = y

ans = []
cnt = 0
for c,a,b in edges:
    if find(a) == find(b):
        continue
    union(a,b)
    ans.append(c)
    cnt += 1
    if cnt == n-1:
        break

print(sum(ans) - max(ans))