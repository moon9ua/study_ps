import sys
input = sys.stdin.readline

n = int(input())
ins = [list(map(int, input().split())) for _ in range(n)]

ins.sort(key=lambda x: (x[1], x[0]))

ret = 0
st = 0
for x,y in ins:
    if x >= st:
        ret += 1
        st = y

print(ret)