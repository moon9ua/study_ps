def solution(sizes):
    mn = 0
    mx = 0
    
    for (x, y) in sizes:
        mn = max(min(x, y), mn)
        mx = max(max(x, y), mx)
    
    return mn * mx