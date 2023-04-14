from collections import defaultdict
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    hs = defaultdict(int)
    for _ in range(n):
        a, b = input().rstrip().split()
        hs[b] += 1
    ret = 1
    for v in hs.values():
        ret *= (v+1)
    print(ret-1)