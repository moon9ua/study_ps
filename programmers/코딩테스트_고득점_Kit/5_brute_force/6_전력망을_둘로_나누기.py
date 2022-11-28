from collections import deque

def solution(n, wires):
    answer = 1e9
    
    graph = [[] for _ in range(n+1)]
    for (a, b) in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    for a, b in wires:
        vis = [False] * (n+1)
        
        q = deque()
        q.append(a)
        vis[a] = True
        vis[b] = True
        ret = 1
        
        while q:
            x = q.popleft()
            for nx in graph[x]:
                if vis[nx] == True:
                    continue
                
                q.append(nx)
                vis[nx] = True
                ret += 1
        
        if abs(ret - (n-ret)) < answer:
            answer = abs(ret - (n-ret))
    
    return answer