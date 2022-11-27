def solution(answers):
    ex = [[1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    ret = [0] * 3
    for i in range(len(answers)):
        for j in range(3):
            if ex[j][i % len(ex[j])] == answers[i]:
                ret[j] += 1
        
    return [i+1 for i in range(3) if ret[i] == max(ret)]