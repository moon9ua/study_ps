import sys
input = sys.stdin.readline

t = int(input())

def isVPS(s):
    st = []
    for c in s:
        if c == '(':
            st.append(c)
        else:
            if not st or st[-1] != '(':
                return 'NO'
            else:
                st.pop()
    if st:
        return 'NO'
    return 'YES'

for _ in range(t):
    s = input().rstrip()
    print(isVPS(s))