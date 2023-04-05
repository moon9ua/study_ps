from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())

nums.sort()

for x in map(int, input().split()):
    print(int(bisect_left(nums, x) != bisect_right(nums, x)))
