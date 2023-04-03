import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

ps = [0] * (n+1)
for i in range(1, n+1):
    ps[i] = ps[i-1] + nums[i-1]

for _ in range(m):
    i, j = map(int, input().split())
    print(ps[j] - ps[i-1])