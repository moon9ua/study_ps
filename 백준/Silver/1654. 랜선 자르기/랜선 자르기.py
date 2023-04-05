import sys
input = sys.stdin.readline

k, n = map(int, input().split())
line = [int(input()) for _ in range(k)]

def ok(x):
    cnt = 0
    for l in line:
        cnt += l // x
    return cnt >= n

l, r = 1, max(line)+1

while l+1 < r:
    mid = (l+r) // 2
    if ok(mid):
        l = mid
    else:
        r = mid

print(l)