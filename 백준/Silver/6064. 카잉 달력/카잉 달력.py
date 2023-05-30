import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m,n,x,y = map(int, input().split())
    
    ans = x
    y = y % n
    while ans <= m*n and ans % n != y:
        ans += m

    if ans > m*n:
        print(-1)
    else:
        print(ans)