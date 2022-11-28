ret = 0

def func(k, dungeons, length):
    global vis, ret
    
    # if k <= 0:
        # ret = max(ret, length)
    if ret < length:
        ret = length
        return
        
    for i, (x, y) in enumerate(dungeons):
        if vis[i] == False and x <= k:
            vis[i] = True
            func(k-y, dungeons, length+1)
            vis[i] = False
            
    # ret = max(ret, length)

def solution(k, dungeons):
    global vis, ret
    vis = [False] * len(dungeons)
    
    func(k, dungeons, 0)
    return ret