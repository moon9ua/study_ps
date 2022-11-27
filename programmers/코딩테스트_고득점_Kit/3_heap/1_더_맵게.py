import heapq

def solution(scoville, K):
    answer = 0
    
    h = []
    for s in scoville:
        heapq.heappush(h, s)
        
    while True:
        a = heapq.heappop(h)
        if a >= K:
            break
        if len(h) == 0:
            return -1
        b = heapq.heappop(h)
        heapq.heappush(h, a + b*2)
        answer += 1
            
    return answer