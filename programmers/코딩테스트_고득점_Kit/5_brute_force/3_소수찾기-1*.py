from itertools import permutations

def is_prime(num):
    if num <= 1:
        return False
    
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
        
    return True

def solution(numbers):
    s = set()
    
    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            s.add(int(''.join(p)))
    
    return sum(1 for elem in s if is_prime(elem))