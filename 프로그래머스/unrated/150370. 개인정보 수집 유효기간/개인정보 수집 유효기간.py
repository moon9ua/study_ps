def solution(today, terms, privacies):
    dict = {t.split()[0]:int(t.split()[1]) for t in terms}

    def get_end(date, t):
        y,m,d = map(int, date.split('.'))
        m += dict[t]
        if m > 12:
            y += m // 12
            m %= 12
        if m == 0:
            y -= 1
            m = 12
        return '.'.join(map(str, [y,m,d]))
        
    def is_delete(end):
        ay,am,ad = map(int, today.split('.'))
        by,bm,bd = map(int, end.split('.'))
        if ay > by:
            return True
        elif ay < by:
            return False
        elif am > bm:
            return True
        elif am < bm:
            return False
        elif ad >= bd:
            return True
        else:
            return False

    answer = []
    for i, p in enumerate(privacies):
        date, t = p.split()
        end = get_end(date, t)
        if is_delete(end):
            answer.append(i+1)
    
    
    return answer