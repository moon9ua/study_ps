import sys
input = sys.stdin.readline

n = int(input())
edges = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(i):
        edges.append((row[j], i, j))
edges.sort()

p = list(range(n))

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

ans = 0
cnt = 0
for c,a,b in edges:
    if find(a) == find(b):
        continue
    union(a,b)
    ans += c
    cnt += 1
    if cnt == n-1:
        break

print(ans)

'''
- find 경로압축 안하면 시간초과
'''