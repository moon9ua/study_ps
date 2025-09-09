### sys input ###

import sys

input = sys.stdin.readline

### solve ###

N, M = map(int, input().split())
n_lst = [0] + list(map(int, input().split()))

prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] + n_lst[i]

for _ in range(M):
    i, j = map(int, input().split())
    print(prefix[j] - prefix[i - 1])
