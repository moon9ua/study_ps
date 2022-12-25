import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

arr = [0] * (n)
arr[0] = nums[0]
for i in range(1, n):
    if arr[i-1] < 0:
        arr[i] = nums[i]
    else:
        arr[i] = arr[i-1] + nums[i]

print(max(arr))