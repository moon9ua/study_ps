import functools

def comp(a, b):
    return int(a+b) - int(b+a)

def solution(numbers):
    nums = list(map(str, numbers))
    
    return str(int(''.join(sorted(nums, key=functools.cmp_to_key(comp), reverse=True))))