import sys
input = sys.stdin.readline

arr = [[0] * 42 for _ in range(2)]
arr[0][0] = 1
arr[1][0] = 0
arr[0][1] = 0
arr[1][1] = 1

'''
arr[0][n] =
arr[1][n] = 
'''

for i in range(2, 41):
    arr[0][i] = arr[0][i-1] + arr[0][i-2]
    arr[1][i] = arr[1][i-1] + arr[1][i-2]

t = int(input())
for _ in range(t):
    n = int(input())
    print(arr[0][n], arr[1][n])
