import sys
input = sys.stdin.readline

k,n = map(int, input().split())
ins = [int(input()) for _ in range(k)]

l,r = 1, max(ins)

while l <= r:
    mid = (l+r) // 2
    cnt = 0

    for lan in ins:
        cnt += lan // mid

    if cnt >= n:
        l = mid + 1
    else:
        r = mid - 1

print(r)

'''
- r = min(ins) 로 했다가 틀림.
'''