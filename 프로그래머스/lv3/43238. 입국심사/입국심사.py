def solution(n, times):
    def Ok(mid):
        cnt = 0
        for time in times:
            cnt += mid // time
        return cnt >= n
    
    l, r = 0, max(times)*n
    
    while l+1 < r:
        mid = (l+r) // 2
        if Ok(mid):
            r = mid
        else:
            l = mid
            
    return r