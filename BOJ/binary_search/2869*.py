a,b,v = map(int, input().split())

l,r = 0,v
ret = 0

while l <= r:
    day = (l+r) // 2

    if v <= a + (day-1)*(a-b):
        r = day - 1
        ret = day
    else:
        l = day + 1

print(ret)