from collections import defaultdict
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
h = defaultdict(str)
for _ in range(n):
    site, pw = input().rstrip().split()
    h[site] = pw

for _ in range(m):
    site = input().rstrip()
    print(h[site])