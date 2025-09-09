### sys input ###

import sys

input = sys.stdin.readline

### solve ###

N = int(input())
P = map(int, input().split())

lst = [0] + sorted(P)
prefix = [0] * (N + 1)

for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] + lst[i]

print(sum(prefix))
