from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    time = [None] + list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    ind = [0] * (n+1)
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        ind[y] += 1
    w = int(input())

    q = deque(i for i in range(1, n+1) if ind[i] == 0)
    dp = [0] * (n+1)
    while q:
        x = q.popleft()
        dp[x] += time[x]
        for nx in graph[x]:
            ind[nx] -= 1
            dp[nx] = max(dp[x], dp[nx])
            if ind[nx] == 0:
                q.append(nx)

    print(dp[w])