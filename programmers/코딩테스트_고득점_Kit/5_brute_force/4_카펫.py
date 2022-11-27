def solution(brown, yellow):
    w, h = yellow, 1
    
    for i in range(2, yellow):
        if w % i != 0:
            continue
        
        if (w//i + 2) * (h*i + 2) - yellow == brown:
            return [w//i + 2, h*i + 2]
    
    return [w+2, h+2]