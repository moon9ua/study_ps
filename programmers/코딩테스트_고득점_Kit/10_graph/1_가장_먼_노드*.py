import collections

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    dist = [-1] * (n+1)
    q = collections.deque()
    q.append(1)
    dist[1] = 0
    
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if dist[nx] != -1:
                continue
            q.append(nx)
            dist[nx] = dist[x] + 1
    
    return dist.count(max(dist))