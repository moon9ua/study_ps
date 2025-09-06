import sys

input = sys.stdin.readline

### solve ###

import math

n, k = map(int, input().split())
ret = math.comb(n, k)
print(ret)
