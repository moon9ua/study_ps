from collections import deque

n, k = map(int, input().split())
q = deque(range(1, n+1))
ret = []

while q:
    for _ in range(k-1):
        q.append(q.popleft())
    ret.append(q.popleft())
    
p = ', '.join(map(str, ret))
print(f'<{p}>')

'''
- #큐

- f string
- join은 str list에만 사용 가능
'''