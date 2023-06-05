import sys
input = sys.stdin.readline

n, m = map(int, input().split())
_, *lst = list(map(int, input().split()))

tr = set(lst)
pts = []

for _ in range(m):
    _, *lst = list(map(int, input().split()))
    pt = set(lst)
    pts.append(pt)

for _ in range(m):
    for pt in pts:
        if tr & pt:
            tr = tr | pt

cnt = 0
for p in pts:
    if not tr & p:
        cnt += 1

print(cnt)