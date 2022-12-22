arr = [[0] * 305 for _ in range(3)]
n = int(input())
nums = [int(input()) for _ in range(n)]

if n == 1: # n == 1 처리 안하면 인덱싱 에러
    print(nums[0])
    exit(0) # 전역에서 return 대신 사용

arr[1][0] = nums[0]
arr[2][0] = 0
arr[1][1] = nums[1]
arr[2][1] = nums[0] + nums[1]

for i in range(2, n):
    arr[1][i] = nums[i] + max(arr[1][i-2], arr[2][i-2])
    arr[2][i] = nums[i] + arr[1][i-1]
    
print(max(arr[1][n-1], arr[2][n-1]))  

'''
n = int(input())
nums = [int(input()) for _ in range(n)]

if n <= 2:
    print(sum(nums))
    exit(0)

d = [0] * n # d[k] = curr + min(d[k-2], d[k-3])
d[0] = nums[0]
d[1] = nums[1]
d[2] = nums[2]

for i in range(3, n):
    d[i] = nums[i] + min(d[i-2], d[i-3])
    
print(sum(nums) - min(d[n-2], d[n-3]))
'''