t = int(input())

arr = [-1] * 15
arr[1] = 1
arr[2] = 2
arr[3] = 4

for i in range(4, 11):
    arr[i] = arr[i-1] + arr[i-2] + arr[i-3]

for _ in range(t):
    n = int(input())
    print(arr[n])
    