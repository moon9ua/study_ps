from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    q = deque(enumerate(nums))
    nums.sort(reverse=True)
    idx = 0
    
    while q:
        i, v = q.popleft()
        if v == nums[idx]:
            if i == m:
                print(idx + 1)
                break
            else:
                idx += 1
        else:
            q.append((i,v))
    