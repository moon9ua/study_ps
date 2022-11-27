from itertools import product

def solution(word):
    lst = []
    
    for i in range(5):
        for p in product('AEIOU', repeat=i+1):
            lst.append(''.join(p))
            
    return sorted(lst).index(word) + 1