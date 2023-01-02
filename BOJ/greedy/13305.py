import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split())) # n-1
cost = list(map(int, input().split())) # n

mn = cost[0]
ret = 0
for i in range(n-1):
    mn = min(mn, cost[i])
    ret += mn * dist[i]

print(ret)