import sys
input = sys.stdin.readline

n = int(input())
homes = [list(map(int, input().split())) for _ in range(n)]
arr = [[0] * 3 for _ in range(n)] # arr = [[0] * n for _ in range(3)] 과 헷갈림 주의

arr[0] = [h for h in homes[0]]

for i in range(1, n):
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + homes[i][0]
    arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + homes[i][1]
    arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + homes[i][2]

print(min(arr[n-1]))