from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

def func(p, dq):
    rev = False
    for c in p:
        if c == 'R':
            rev = not rev
        else:
            if not dq:
                return 'error'
            if rev:
                dq.pop()
            else:
                dq.popleft()
    
    if rev:
        dq.reverse()
    return f'[{",".join(map(str, dq))}]'

for _ in range(t):
    p = input().rstrip()
    n = int(input())
    nums = input().rstrip()
    
    if n:
        dq = deque(map(int, nums[1:-1].split(',')))
    else:
        dq = deque()
        
    print(func(p, dq))

'''
- `dq = deque(map(int, nums[1:-1].split(',')))`
    - n=0 [] 인 경우에 dq를 만들 때 오류 발생. ''에 int를 적용해서 그런가?
'''