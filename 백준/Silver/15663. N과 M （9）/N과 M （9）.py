import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

used = [False] * n
lst = []
ans = []
def func(k):
    if k == m:
        ans.append(' '.join(map(str, lst)))
        return

    for i in range(n):
        if not used[i]:
            lst.append(nums[i])
            used[i] = True
            func(k+1)
            lst.pop()
            used[i] = False

func(0)
print(*dict.fromkeys(ans), sep='\n')