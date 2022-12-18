import sys
input = sys.stdin.readline

n = int(input())
st = []

for _ in range(n):
    cmd = input().rstrip()

    if cmd == 'pop':
        if not st:
            print(-1)
        else:
            print(st.pop())
    elif cmd == 'size':
        print(len(st))
    elif cmd == 'empty':
        print(int(len(st) == 0))
    elif cmd == 'top':
        if not st:
            print(-1)
        else:
            print(st[-1])
    else:
        _, x = cmd.split()
        st.append(x)


'''
- #스택

- sys readline, rstrip
- not <list>: length == 0인지 여부
- <list>.pop()
'''