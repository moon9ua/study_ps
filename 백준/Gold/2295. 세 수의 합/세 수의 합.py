from itertools import combinations_with_replacement
from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n = int(input())
u = [int(input()) for _ in range(n)]
u.sort()

two = []
for i in range(n):
    for j in range(n):
        two.append(u[i] + u[j])
two.sort()

for i in range(n-1, -1, -1):
    for j in range(i):
        target = u[i] - u[j]
        cnt = bisect_right(two, target) - bisect_left(two, target)
        if cnt:
            print(u[i])
            exit()