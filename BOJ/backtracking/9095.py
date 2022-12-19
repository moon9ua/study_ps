t = int(input())

ret = 0

def func(s):
    global ret
    if s < 0:
        return
    if s == 0:
        ret += 1
        return
    func(s-1)
    func(s-2)
    func(s-3)

for _ in range(t):
    n = int(input())
    func(n)
    print(ret)
    ret = 0
