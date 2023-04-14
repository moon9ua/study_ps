import heapq

def solution(jobs):
    pq = []
    cnt = 0
    st = -1
    curr = 0
    tot = 0
    while cnt < len(jobs):
        for j in jobs:
            if st < j[0] <= curr:
                heapq.heappush(pq, (j[1],j[0]))
        if pq:
            job = heapq.heappop(pq)
            st = curr
            curr += job[0]
            tot += curr - job[1]
            cnt += 1
        else:
            curr += 1
    
    return tot // len(jobs)