import sys
input = sys.stdin.readline

m, n = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def ok(mid):
    if mid == 0:
        return False
    cnt = 0
    for i in range(n):
        cnt += (arr[i] // mid)
    return cnt >= m

l, r = 0, arr[-1] + 1

while l+1 < r:
    mid = (l+r)//2
    if ok(mid):
        l = mid
    else:
        r = mid

print(l)