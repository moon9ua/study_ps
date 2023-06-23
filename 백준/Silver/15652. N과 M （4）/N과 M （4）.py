n, m = map(int, input().split())

lst = []
def func(st, k):
    if k == m:
        print(*lst)
        return

    for i in range(st, n+1):
        lst.append(i)
        func(i, k+1)
        lst.pop()

func(1, 0)