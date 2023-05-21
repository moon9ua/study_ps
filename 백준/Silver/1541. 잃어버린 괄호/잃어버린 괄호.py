s = input()
ans = 0

def calc(st):
    strs = st.split('+')
    ret = 0
    for s in strs:
        ret += int(s)
    return ret

strs = s.split('-')
ans += calc(strs[0])

if len(strs) > 1:
    for st in strs[1:]:
        ans -= calc(st)

print(ans)