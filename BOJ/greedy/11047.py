import sys
input = sys.stdin.readline

n,k = map(int, input().split())
coin = [int(input()) for _ in range(n)]

ret = 0
for c in coin[::-1]:
    if k // c:
        ret += k // c
        k = k % c

print(ret)