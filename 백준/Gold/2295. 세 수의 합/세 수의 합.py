from itertools import combinations_with_replacement
from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n = int(input())
u = [int(input()) for _ in range(n)]

two = []
for i in range(n):
    for j in range(n):
        two.append(u[i] + u[j])
two.sort()

mx = 0
for i in range(n):
    for j in range(i):
        target = u[i] - u[j]
        cnt = bisect_right(two, target) - bisect_left(two, target)
        if cnt:
            mx = max(mx, u[i])

print(mx)