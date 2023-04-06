import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

def Ok(mid):
    tot = 0
    for a in arr:
        if a >= mid:
            tot += a-mid
    return tot >= m

l, r = 0, max(arr)+1
while l+1 < r:
    mid = (l+r) // 2
    if Ok(mid):
        l = mid
    else:
        r = mid
print(l)