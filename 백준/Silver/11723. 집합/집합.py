import sys
input = sys.stdin.readline

s = set()

m = int(input())
for _ in range(m):
    cmds = input().rstrip().split()

    if cmds[0] == 'add':
        s.add(int(cmds[1]))
    elif cmds[0] == 'remove':
        s.discard(int(cmds[1]))
    elif cmds[0] == 'check':
        print(int(int(cmds[1]) in s))
    elif cmds[0] == 'toggle':
        if int(cmds[1]) in s:
            s.remove(int(cmds[1]))
        else:
            s.add(int(cmds[1]))
    elif cmds[0] == 'all':
        s = set(range(1, 21))
    elif cmds[0] == 'empty':
        s = set()
