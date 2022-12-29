import sys
input = sys.stdin.readline

n,m = map(int, input().split())
ins = list(map(int, input().split()))

l, r = 0, max(ins)

while l <= r:
    h = (l+r) // 2
    tot = 0
    
    for tree in ins:
        if tree > h:
            tot += tree - h

    if tot >= m:
        l = h + 1
    else:
        r = h - 1

print(r)