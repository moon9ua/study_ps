import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()
target = 'IO' * n + 'I'

cnt = 0
l = 2*n + 1
for i in range(m - l + 1):
    sub = s[i:i+l]
    if sub == target:
        cnt += 1

print(cnt)