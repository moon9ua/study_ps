import collections

def solution(nums):
    hash = collections.Counter(nums)
    
    return min(len(hash), len(nums) // 2)