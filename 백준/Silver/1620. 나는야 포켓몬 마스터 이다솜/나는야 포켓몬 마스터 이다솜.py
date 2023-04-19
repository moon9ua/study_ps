from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
pk = [None]
dt = defaultdict(int)
for i in range(1, n+1):
    name = input().rstrip()
    pk.append(name)
    dt[name] = i

for _ in range(m):
    cmd = input().rstrip()
    if cmd.isdecimal():
        print(pk[int(cmd)])
    else:
        print(dt[cmd])