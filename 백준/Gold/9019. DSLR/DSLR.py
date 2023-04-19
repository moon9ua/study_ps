from collections import deque
import sys
input = sys.stdin.readline

def convert(x):
    ret = []
    ret.append(x*2 % 10000)
    ret.append(x-1 if x-1 >= 0 else 9999)

    s = str(x).zfill(4)
    ret.append(int(s[1:] + s[0]))
    ret.append(int(s[3] + s[:3]))
    return ret

command = 'DSLR'

t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    
    q = deque()
    vis = [False] * 10005

    q.append((a, ''))
    vis[a] = True
    while q:
        x,path = q.popleft()
        if x == b:
            print(path)
            break
        for i,nx in enumerate(convert(x)):
            if vis[nx]:
                continue
            q.append((nx, path+command[i]))
            vis[nx] = True