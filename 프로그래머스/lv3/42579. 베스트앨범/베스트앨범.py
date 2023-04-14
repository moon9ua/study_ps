from collections import defaultdict

def solution(genres, plays):
    ret = []
    
    dt = defaultdict(list)
    for i in range(len(plays)):
        dt[genres[i]].append((plays[i], i))
    
    # list_dt = sorted(dt.items(), key=lambda x:sum(x[1]))
    list_dt = sorted(dt.items(), key=lambda x:-sum([e[0] for e in x[1]]))
    
    for _,lst in list_dt:
        lst.sort(key=lambda x:(-x[0], x[1]))
        ret += [e[1] for e in lst[:2]]
    
    return ret