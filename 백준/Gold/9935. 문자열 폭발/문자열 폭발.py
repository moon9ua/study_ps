import sys
input = sys.stdin.readline

s = input().rstrip()
b = input().rstrip()

lb = len(b)
st = []

def isbomb():
    if len(st) < lb:
        return False

    for i in range(lb):
        if not st[-1-i] or st[-1-i] != b[-1-i]:
            return False

    return True

for char in s:
    st.append(char)

    if isbomb():
        for i in range(lb):
            st.pop()

print(''.join(st) if st else 'FRULA')
