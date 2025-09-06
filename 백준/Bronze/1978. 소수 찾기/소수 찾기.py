import math

def is_target(num):
    if num == 1:
        return False
    for i in range(2, num):
        if i > math.sqrt(num):
            continue
        if num % i == 0:
            return False
    return True

n = int(input())
nums = map(int, input().split())

cnt = 0
for num in nums:
    cnt += is_target(num)

print(cnt)