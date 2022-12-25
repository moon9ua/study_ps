import sys
input = sys.stdin.readline

n = int(input())
ins = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if ins[i] > ins[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))