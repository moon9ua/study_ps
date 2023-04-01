from itertools import combinations

n, m = map(int, input().split())
for cb in combinations(range(1, n+1), m):
    print(*cb)