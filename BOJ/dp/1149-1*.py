import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

arr = [[0]*3 for _ in range(n)]
arr[0] = cost[0]

for i in range(1, n):
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + cost[i][0]
    arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + cost[i][1]
    arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + cost[i][2]
    
print(min(arr[n-1]))