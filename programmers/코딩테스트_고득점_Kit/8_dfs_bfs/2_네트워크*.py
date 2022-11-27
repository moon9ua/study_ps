from collections import deque

def solution(n, computers):
    vis = [False] * n
    ret = 0
    q = deque()
    
    for i in range(n):
        if vis[i] == True:
            continue
            
        vis[i] = True
        q.append(i)
        ret += 1
        
        while q:
            x = q.popleft()
            
            for j, v in enumerate(computers[x]):
                if v == 0 or i == j:
                    continue
                if j < 0 or j >= n:
                    continue
                if vis[j] == True:
                    continue
                
                vis[j] = True
                q.append(j)
    
    return ret