ret = 0

def func(k, numbers, target):
    global ret
    
    if k == len(numbers):
        if target == 0:
            ret += 1
        return
    
    func(k+1, numbers, target+numbers[k])
    func(k+1, numbers, target-numbers[k])

def solution(numbers, target):
    func(0, numbers, target)
    
    return ret