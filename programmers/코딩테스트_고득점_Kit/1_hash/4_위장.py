import collections

def solution(clothes):
    dict = collections.defaultdict(list)
    
    for v, k in clothes:
        dict[k].append(v)
    
    ret = 1
    
    for x in list(dict.values()):
        ret *= len(x) + 1
        
    return ret - 1