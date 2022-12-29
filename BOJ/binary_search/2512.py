import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

l, r = 0, max(arr)
ret = 0

while l <= r:
    mid = (l+r) // 2
    tot = 0
    mx = 0

    for a in arr:
        if a >= mid:
            tot += mid
            mx = max(mx, mid)
        else:
            tot += a
            mx = max(mx, a)
    
    if tot <= m:
        l = mid + 1
        ret = mx
    else:
        r = mid - 1

print(ret)

'''
- l, r 첫설정이 중요함. l을 0으로 안했다가 틀렸었음.
'''