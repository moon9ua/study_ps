n = int(input())

def isvalid(s):
    l = 2
    while l <= len(s):
        st = len(s) - l
        md = st + l//2
        end = st + l
        if s[st:md] == s[md:end]:
            return False
        l += 2
    return True

ret = None

def func(k, s):
    global ret

    if ret:
        return

    if k == n:
        ret = s
        return
        
    for i in range(1, 4):
        if isvalid(s+str(i)):
            func(k+1, s+str(i))

func(0, '')
print(ret)