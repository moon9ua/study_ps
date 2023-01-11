import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
d = [[1e9]*(n+1) for _ in range(n+1)]
nxt = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    d[a][b] = min(d[a][b], c)
    nxt[a][b] = b
for i in range(1,n+1):
    d[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if d[i][k]+d[k][j] < d[i][j]:
                d[i][j] = d[i][k]+d[k][j]
                nxt[i][j] = nxt[i][k]

for i in range(1,n+1):
    print(*[0 if k == 1e9 else k for k in d[i][1:]])

for i in range(1,n+1):
    for j in range(1,n+1):
        if d[i][j] == 0 or d[i][j] == 1e9:
            print(0)
            continue
        
        path = []
        st = i
        while st != j:
            path.append(st)
            st = nxt[st][j]
        path.append(j)

        print(len(path), end=' ')
        print(*path)