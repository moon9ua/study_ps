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

    for i in range(n):
        if not used[i]:
            lst.append(nums[i])
            used[i] = True
            func(k+1)
            lst.pop()
            used[i] = False

func(0)