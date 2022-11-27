from collections import Counter

def solution(participant, completion):
    hash = Counter(completion)
    
    for p in participant:
        if hash[p] == 0:
            return p
        hash[p] -= 1
