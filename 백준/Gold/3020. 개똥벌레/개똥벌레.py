import sys
input = sys.stdin.readline

n, h = map(int, input().split())

top = [0] * (h+1)
bottom = [0] * (h+1)

for i in range(n):
    if i % 2 == 0:
        bottom[int(input())] += 1
    else:
        top[int(input())] += 1

for i in range(h-1, 0, -1):
    bottom[i] += bottom[i+1]
    top[i] += top[i+1]

ret = []

for i in range(1, h+1):
    tot = bottom[i] + top[h-i+1]
    ret.append(tot)

print(min(ret), ret.count(min(ret)))