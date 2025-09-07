### sys input ###

import sys

input = sys.stdin.readline

### solve ###


N, r, c = map(int, input().split())


def find_ord(x, y, n):
    if n == 0:
        return 0

    half = 2 ** (n - 1)
    quarter = 2 ** (2 * n - 2)

    if x < half and y < half:
        return find_ord(x, y, n - 1)
    elif x < half and y >= half:
        return find_ord(x, y - half, n - 1) + quarter
    elif x >= half and y < half:
        return find_ord(x - half, y, n - 1) + quarter * 2
    else:
        return find_ord(x - half, y - half, n - 1) + quarter * 3


ret = find_ord(r, c, N)

print(ret)
