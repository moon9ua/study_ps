import sys
input = sys.stdin.readline

n = int(input())
wine = [int(input()) for _ in range(n)]

arr = [[0]*3 for _ in range(n)]

arr[0][0] = 0
arr[0][1] = wine[0]
arr[0][2] = 0

for i in range(1, n):
    arr[i][0] = max(arr[i-1])
    arr[i][1] = arr[i-1][0] + wine[i]
    arr[i][2] = arr[i-1][1] + wine[i]

print(max(arr[n-1]))