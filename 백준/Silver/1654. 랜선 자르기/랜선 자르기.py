### sys input ###

import sys

input = sys.stdin.readline

### solve ###

K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

l = 1
r = max(lines)


def ok(mid):
    cnt = 0
    for line in lines:
        cnt += line // mid
    return cnt >= N


ans = 0

while l <= r:
    mid = (l + r) // 2

    if ok(mid):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)
