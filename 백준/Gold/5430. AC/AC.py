from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = input().rstrip()
    n = int(input())
    nums = deque(num for num in input().rstrip()[1:-1].split(',') if num != '')
    rev = False
    err = False

    for c in p:
        if c == 'R':
            rev = not rev
        else:
            if not nums:
                print('error')
                err = True
                break
            if not rev:
                nums.popleft()
            else:
                nums.pop()

    if err:
        continue

    if not rev:
        print(f"[{','.join(nums)}]")
    else:
        nums.reverse()
        print(f"[{','.join(nums)}]")
