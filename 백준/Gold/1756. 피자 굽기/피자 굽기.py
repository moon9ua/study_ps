import sys
input = sys.stdin.readline

d, n = map(int, input().split())
oven = list(map(int, input().split()))
pizza = list(map(int, input().split()))

arr = [oven[0]]
for i in range(1, d):
    arr.append(min(oven[i], arr[i-1]))

def Ok(mid, p):
    if arr[mid] >= p:
        return True
    else:
        return False

ed = d-1
for p in pizza:
    l, r = 0, ed
    if not Ok(l, p):
        print(0)
        exit()
    if Ok(r, p):
        ed -=1
        continue
    while l+1 < r:
        mid = (l+r) // 2
        if Ok(mid, p):
            l = mid
        else:
            r = mid
    ed = l-1

print(ed+2)