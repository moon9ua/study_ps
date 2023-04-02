from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline
dx = [-1,0,1,0]
dy = [0,-1,0,1]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

st = None
food_cnt = 0

for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            continue
        elif board[i][j] == 9:
            st = (i,j)
            board[i][j] = 0
        else:
            food_cnt += 1

time = 0
size = 2
rest = size

def calc_next(next_points):
    ans = next_points[0]
    for p in next_points:
        if p[0] < ans[0]:
            ans = p
        elif p[0] == ans[0] and p[1] < ans[1]:
            ans = p
    return ans

while food_cnt:
    q = deque()
    dist = [[-1]*n for _ in range(n)]
    next_points = []
    min_dist = 1e9
    
    q.append(st)
    dist[st[0]][st[1]] = 0
    while q and food_cnt:
        x,y = q.popleft()
        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if dist[nx][ny] != -1 or board[nx][ny] > size:
                continue
            dist[nx][ny] = dist[x][y] + 1
            if board[nx][ny] and board[nx][ny] < size and min_dist >= dist[nx][ny]:
                min_dist = dist[nx][ny]
                next_points.append((nx,ny))
                continue
            q.append((nx,ny))

    if not next_points:
        break

    nx, ny = calc_next(next_points)
    time += dist[nx][ny]
    st = (nx, ny)
    food_cnt -= 1
    rest -= 1
    if not rest:
        size += 1
        rest = size
    board[nx][ny] = 0

print(time)