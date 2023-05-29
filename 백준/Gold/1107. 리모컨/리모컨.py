import sys
input = sys.stdin.readline

def func():
    n = int(input())
    m = int(input())
    mn = abs(n - 100)

    if not m:
        mn = min(mn, len(str(n)))
        print(mn)
        return

    err = input().rstrip().split()

    for i in range(999999 + 1):
        if set(str(i)) & set(err):
            continue
        mn = min(mn, len(str(i)) + abs(n - i))

    print(mn)

func()