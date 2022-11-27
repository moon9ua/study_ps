from collections import deque

def solution(begin, target, words):
    vis = [False] * len(words)
    
    q = deque()
    q.append((begin, 0))
    
    while q:
        cur, k = q.popleft()
        if cur == target:
            return k
        
        for i, word in enumerate(words):
            if vis[i]:
                continue
            
            diff = 0
            for j in range(len(word)):
                if cur[j] != word[j]:
                    diff += 1
            if diff != 1:
                continue
                
            q.append((word, k+1))
            vis[i] = True
                
    return 0