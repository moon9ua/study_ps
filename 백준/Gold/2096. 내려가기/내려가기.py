import sys
input = sys.stdin.readline

n = int(input())

mx = [0] * 3
mn = [0] * 3

for i in range(n):
    row = list(map(int, input().split()))
    new_mx = [0] * 3
    new_mn = [0] * 3

    new_mx[0] = max(mx[0], mx[1]) + row[0]
    new_mx[1] = max(mx) + row[1]
    new_mx[2] = max(mx[1], mx[2]) + row[2]

    new_mn[0] = min(mn[0], mn[1]) + row[0]
    new_mn[1] = min(mn) + row[1]
    new_mn[2] = min(mn[1], mn[2]) + row[2]

    mx = new_mx
    mn = new_mn

print(max(mx), min(mn))