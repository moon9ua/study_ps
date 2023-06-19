from collections import deque

n, k = map(int, input().split())
dist = [-1] * 100005
q = deque()
dist[n] = 0
q.append(n)

def process():
    global n, k
    
    if n == k:
        return 0
    
    while q:
        x = q.popleft()
        
        for nx in [x-1, x+1, x*2]:
            if nx < 0 or nx > 100000:
                continue
            if dist[nx] != -1:
                continue
            if nx == k:
                return dist[x] + 1
            dist[nx] = dist[x] + 1
            q.append(nx)
        
print(process())