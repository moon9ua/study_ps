import collections
import math

def solution(progresses, speeds):
    ret = []
    q = collections.deque(zip(progresses, speeds))
    day = 1
    count = 0
    
    while q:
        p, s = q[0]
        if p + s * day >= 100:
            count += 1
            q.popleft()
        else:
            if count:
                ret.append(count)
                count = 0
            day = math.ceil((100 - p) / s)
    
    if count:
        ret.append(count)
    
    return ret