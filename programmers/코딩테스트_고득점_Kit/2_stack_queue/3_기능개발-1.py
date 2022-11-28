from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    
    q = deque()
    for tp in zip(progresses, speeds):
        q.append(tp)
        
    day = 1
    ret = 0
    while q:
        p, s = q.popleft()
        if p + s*day >= 100:
            ret += 1
        else:
            day = math.ceil((100 - p) / s)
            # 틀린 풀이: day = (101 - p) // s
            # 맞는 풀이: day = (100 - p + s - 1) // s
            if ret:
                answer.append(ret)
            ret = 1
            
    if ret:
        answer.append(ret)
        
    return answer