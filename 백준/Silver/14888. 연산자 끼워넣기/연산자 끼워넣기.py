import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))

mx = -1e9
mn = 1e9

def calc(i, a, b):
    if i == 0:
        return a + b
    elif i == 1:
        return a - b
    elif i == 2:
        return a * b
    else:
        if a < 0 and b > 0:
            return -(-a // b)
        return a // b

def func(k, curr):
    global mx, mn

    if k == n-1:
        mx = max(mx, curr)
        mn = min(mn, curr)
        return

    for i in range(4):
        if not op[i]:
            continue
        op[i] -= 1
        func(k+1, calc(i, curr, nums[k+1]))
        op[i] += 1

func(0, nums[0])
print(mx)
print(mn)