import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

lst = []
def func(st, k):
    if k == m:
        print(*lst)
        return

    prev = 0
    for i in range(st, n):
        if prev != nums[i]:
            lst.append(nums[i])
            prev = nums[i]
            func(i, k+1)
            lst.pop()

func(0, 0)