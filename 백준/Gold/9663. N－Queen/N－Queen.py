n = int(input())

visited = []
cnt = 0

def check(r, c):
    for x, y in visited:
        if c == y or x-y == r-c or x+y == r+c:
            return False
    return True


def func(r):
    global cnt

    if r == n:
        cnt += 1

    for c in range(n):
        if check(r, c):
            visited.append((r, c))
            func(r+1)
            visited.pop()

func(0)
print(cnt)