import sys
input = sys.stdin.readline

n, k = map(int, input().split())

ws = []
vs = []
for _ in range(n):
    w, v = map(int, input().split())
    ws.append(w)
    vs.append(v)

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for w in range(1, k+1):
        if w-ws[i-1] >= 0:
            dp[i][w] = max(vs[i-1]+dp[i-1][w-ws[i-1]], dp[i-1][w])
        else:
            dp[i][w] = dp[i-1][w]

print(dp[n][k])