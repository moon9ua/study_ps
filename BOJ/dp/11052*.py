import sys
input = sys.stdin.readline

n = int(input())
cost = [0] + list(map(int, input().split()))

dp = [0] * (n+1)

for i in range(1, n+1):
    for j in range(0, i):
        dp[i] = max(dp[i], dp[j] + cost[i-j])

print(dp[n])

'''
- 이중 반복문 dp
- 리스트 깊은복사
'''