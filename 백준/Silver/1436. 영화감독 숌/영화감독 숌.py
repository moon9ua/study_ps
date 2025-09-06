import sys

input = sys.stdin.readline

### solve ###

n = int(input())

cnt = 0
ret = None
i = 1
while cnt < n:
    str_i = str(i)
    if "666" in str_i:
        cnt += 1
        ret = i
    i += 1

print(ret)
