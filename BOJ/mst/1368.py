import sys
input = sys.stdin.readline

n = int(input())
e = []
for i in range(n):
    c = int(input())
    e.append((c,i,n))
for i in range(n):
    ins = list(map(int, input().split()))
    for j in range(i):
        e.append((ins[j], i, j))
e.sort()

n += 1

p = [i for i in range(n)]

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(a,b):
    x = find(a)
    y = find(b)
    if x < y:
        p[y] = x
    else:
        p[x] = y

cnt = 0
ret = 0
for edge in e:
    c,a,b = edge
    if find(a) == find(b):
        continue
    union(a,b)
    ret += c
    cnt += 1
    if cnt == n-1:
        break

print(ret)