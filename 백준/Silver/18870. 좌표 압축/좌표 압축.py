from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))

tmp = sorted(list(set(x)))

for xi in x:
    print(bisect_left(tmp, xi), end=' ')