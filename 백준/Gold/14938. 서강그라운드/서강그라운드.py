import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
items = [None] + list(map(int, input().split()))
d = [[1e9]*(n+1) for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    d[a][b] = l
    d[b][a] = l

for i in range(1, n+1):
    d[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            d[i][j] = min(d[i][j], d[i][k]+d[k][j])

mx = 0
for i in range(1, n+1):
    s = sum(items[j] for j in range(1, n+1) if d[i][j] <= m)
    mx = max(mx, s)

print(mx)