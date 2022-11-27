rets = []
ret = ['ICN']

def func(tickets):
    if len(ret) == len(tickets) + 1:
        rets.append(ret[::])
        return
    
    for i, (a, b) in enumerate(tickets):
        if used[i] == True or ret[-1] != a:
            continue
            
        ret.append(b)
        used[i] = True
        func(tickets)
        ret.pop()
        used[i] = False

def solution(tickets):
    global used
    used = [False] * len(tickets)
    
    func(tickets)
    return sorted(rets)[0]