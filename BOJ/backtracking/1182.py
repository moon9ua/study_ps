from itertools import combinations

n, s = map(int, input().split())
nums = list(map(int, input().split()))

ret = 0
for i in range(1, n+1):
    for c in combinations(nums, i):
        if sum(c) == s:
            ret += 1
            
print(ret)

'''
- #조합

- map은 iterator이므로 값이 소모됨.
'''