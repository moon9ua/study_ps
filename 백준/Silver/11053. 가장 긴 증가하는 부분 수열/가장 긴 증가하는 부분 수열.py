import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    mx = 1
    for j in range(i):
        if a[j] < a[i]:
            mx = max(mx, dp[j]+1)
    dp[i] = mx

print(max(dp))