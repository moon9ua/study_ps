from collections import deque

def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for (x, y) in wires:
        graph[x].append(y)
        graph[y].append(x)
    
    ret = 1e9
    
    for (x, y) in wires:
        q = deque()
        q.append(x)
        vis = [False] * (n+1)
        vis[x] = True
        vis[y] = True
        cnt = 1
        
        while q:
            a = q.popleft()
            for na in graph[a]:
                if vis[na] == True:
                    continue
                q.append(na)
                cnt += 1
                vis[na] = True
        
        if abs(cnt - (n-cnt)) < ret:
            ret = abs(cnt - (n-cnt))
            
    return ret