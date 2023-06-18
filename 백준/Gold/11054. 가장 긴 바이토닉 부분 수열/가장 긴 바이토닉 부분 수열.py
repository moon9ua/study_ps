import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp = [[0] * n for _ in range(2)]

for i in range(n):
    mx1, mx2 = 1, 1
    for j in range(i):
        if a[j] < a[i]:
            mx1 = max(mx1, dp[0][j] + 1)
        if a[j] > a[i]:
            mx2 = max(mx2, dp[0][j] + 1, dp[1][j] + 1)
    dp[0][i] = mx1
    dp[1][i] = mx2

print(max(map(max, dp)))