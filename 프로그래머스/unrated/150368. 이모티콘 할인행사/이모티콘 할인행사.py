from itertools import product

def solution(users, emoticons):
    ret = [0, 0]
    costs = [0] * len(users)
    percent = []
    
    def func(k):
        nonlocal ret, costs
        
        if k == len(emoticons):
            cnt = 0
            tot = 0
            for i in range(len(users)):
                _, limit = users[i]
                if limit <= costs[i]:
                    cnt += 1
                else:
                    tot += costs[i]
            if ret[0] < cnt:
                ret = [cnt, tot]
            elif ret[0] == cnt:
                ret = [cnt, max(ret[1], tot)]
            return
        
        for p in [10,20,30,40]:
            for i in range(len(users)):
                if users[i][0] <= p:
                    costs[i] += int(emoticons[k] * (100-p) / 100)
            percent.append(p)
            func(k+1)
            for i in range(len(users)):
                if users[i][0] <= p:
                    costs[i] -= int(emoticons[k] * (100-p) / 100)
            percent.pop()
    
    func(0)
    return ret