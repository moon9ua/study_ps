from collections import deque
import sys

input = sys.stdin.readline
dx = [1,0,0,-1,0,0]
dy = [0,1,0,0,-1,0]
dz = [0,0,1,0,0,-1]

while True:
    l,r,c = map(int, input().split())
    if l == 0:
        break
    
    board = []
    for i in range(l):
        floor = []
        for j in range(r):
            row = input().rstrip()
            if 'S' in row:
                st = (i,j,row.index('S'))
            # if 'E' in row:
                # ed = (i,j,row.index('E'))
            floor.append(row)
        board.append(floor)
        input()
    
    dist = [[[-1]*c for _ in range(r)] for _ in range(l)]
    
    q = deque()
    q.append(st)
    s1,s2,s3 = st
    dist[s1][s2][s3] = 0

    ans = None
    while q:
        x,y,z = q.popleft()
        if board[x][y][z] == 'E':
            ans = dist[x][y][z]
            break
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or ny < 0 or nz < 0 or \
                nx >= l or ny >= r or nz >= c:
                continue
            if dist[nx][ny][nz] != -1 or \
                board[nx][ny][nz] == '#':
                continue
            q.append((nx,ny,nz))
            dist[nx][ny][nz] = dist[x][y][z] + 1

    if ans:
        print(f'Escaped in {ans} minute(s).')
    else:
        print('Trapped!')

'''
- 3차원 string board
'''