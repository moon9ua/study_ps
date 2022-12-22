import sys
input = sys.stdin.readline

n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]

arr = [[0]*n for _ in range(n)]
arr[0][0] = tri[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            arr[i][j] = arr[i-1][j] + tri[i][j]
        elif j == i:
            arr[i][j] = arr[i-1][j-1] + tri[i][j]
        else:
            arr[i][j] = max(arr[i-1][j-1], arr[i-1][j]) + tri[i][j]

print(max(arr[n-1]))
