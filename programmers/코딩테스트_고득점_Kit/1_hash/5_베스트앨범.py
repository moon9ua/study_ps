import collections

def solution(genres, plays):
    cnt = collections.Counter()
    dict = collections.defaultdict(list)
    for i, v in enumerate(genres):
        cnt[v] += plays[i]
        dict[v].append((-plays[i], i))
        
    answer = []
    for g, _ in cnt.most_common():
        answer += [i for (_, i) in sorted(dict[g])[:2]]
        
    return answer