import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

used = [False] * n
lst = []
def func(k):
    if k == m:
        print(*lst)
        return

    prev = 0
    for i in range(n):
        if not used[i] and prev != nums[i]:
            lst.append(nums[i])
            used[i] = True
            prev = nums[i]
            func(k+1)
            lst.pop()
            used[i] = False

func(0)