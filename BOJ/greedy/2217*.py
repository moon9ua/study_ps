import sys
input = sys.stdin.readline

n = int(input())
ins = [int(input()) for _ in range(n)]

ins.sort(reverse=True)

ret = 0

for i in range(n):
    mx = ins[i] * (i+1)
    ret = max(ret, mx)

print(ret)

'''
- 반례 조심: 중간에 break 하면 틀림
5
1
1
1
3
1
'''