import sys
input = sys.stdin.readline

n = int(input())
d = []
for _ in range(n):
    row = list(map(int, input().split()))
    d.append([r if r != 0 else 1e9 for r in row])

for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k]+d[k][j])

for i in range(n):
    for j in range(n):
        if d[i][j] == 1e9:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()