import sys
input = sys.stdin.readline

v,e = map(int, input().split())
edges = []
for _ in range(e):
    a,b,c = map(int, input().split())
    edges.append((c,a,b))
edges.sort()

p = [i for i in range(v+1)]

def find(x):
    if p[x] == x:
        return x
    return find(p[x])

def union(a, b):
    x = find(a)
    y = find(b)
    if x < y:
        p[y] = x
    else:
        p[x] = y

ret = 0
cnt = 0
for edge in edges:
    c,a,b = edge
    if find(a) == find(b):
        continue
    union(a,b)
    ret += c
    cnt += 1
    if cnt == v-1:
        break

print(ret)