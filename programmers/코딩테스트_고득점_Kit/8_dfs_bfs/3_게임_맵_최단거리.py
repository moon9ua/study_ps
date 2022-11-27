from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    q = deque()
    q.append((0, 0))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
                
            if maps[nx][ny] != 1:
                continue
            
            q.append((nx, ny))
            maps[nx][ny] = maps[x][y] + 1
            
    if maps[-1][-1] == 1 or maps[-1][-1] == 0:
        return -1
            
    return maps[-1][-1]