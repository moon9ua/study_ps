from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
d = deque()

for _ in range(n):
    cmd = input().rstrip()
    
    if cmd == 'pop_front':
        if not d:
            print(-1)
        else:
            print(d.popleft())
    elif cmd == 'pop_back':
        if not d:
            print(-1)
        else:
            print(d.pop())
    elif cmd == 'size':
        print(len(d))
    elif cmd == 'empty':
        print(int(not d))
    elif cmd == 'front':
        if not d:
            print(-1)
        else:
            print(d[0])
    elif cmd == 'back':
        if not d:
            print(-1)
        else:
            print(d[-1])
    else:
        c, x = cmd.split()
        if c == 'push_front':
            d.appendleft(x)
        else:
            d.append(x)