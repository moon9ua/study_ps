N,r,c = map(int, input().split())

def func(n, x, y):
    if n == 0:
        return 0

    if x < 2**(n-1) and y < 2**(n-1):
        return func(n-1, x, y)
    elif x < 2**(n-1) and y >= 2**(n-1):
        return 2**((n-1)*2) + func(n-1, x, y-2**(n-1))
    elif x >= 2**(n-1) and y < 2**(n-1):
        return 2**((n-1)*2)*2 + func(n-1, x-2**(n-1), y)
    else:
        return 2**((n-1)*2)*3 + func(n-1, x-2**(n-1), y-2**(n-1))

print(func(N,r,c))