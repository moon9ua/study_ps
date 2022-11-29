from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

lst.sort(key=lambda x: x[::-1])

q = deque(lst)
st = 0
ret = 0
while q:
    x, y = q.popleft()
    if st <= x:
        ret += 1
        st = y
        
print(ret)

'''
import sys
input = sys.stdin.readline

n = int(input())
lst = [tuple(map(int, input().split())) for _ in range(n)]

lst.sort(key=lambda x: (x[1], x[0]))

ret = 0
st = 0

for (x, y) in lst:
    if x < st:
        continue
    
    st = y
    ret += 1

print(ret)
'''