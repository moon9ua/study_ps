from collections import defaultdict

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

fst = nums[:n//2]
scd = nums[n//2:]

fmap = defaultdict(int)
smap = defaultdict(int)

lst = []
def func(arr, i, ed):
    if i == ed:
        if arr is fst:
            fmap[sum(lst)] += 1
        else:
            smap[sum(lst)] += 1
        return

    lst.append(arr[i])
    func(arr, i+1, ed)
    lst.pop()
    func(arr, i+1, ed)

func(fst, 0, n//2)
func(scd, 0, n - n//2)

ret = 0
for k, v in smap.items():
    if s-k in fmap:
        ret += v * fmap[s-k]

if s == 0:
    ret -= 1

print(ret)
