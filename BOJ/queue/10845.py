from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque()

for _ in range(n):
    cmd = input().rstrip()
    
    if cmd == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif cmd == 'size':
        print(len(q))
    elif cmd == 'empty':
        print(int(not q))
    elif cmd == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif cmd == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])
    else:
        _, x = cmd.split()
        q.append(x)