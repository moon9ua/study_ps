from itertools import combinations

while True:
    k, *s = list(map(int, input().split()))
    if k == 0:
        break
    
    for c in combinations(s, 6):
        print(*c)
    print()

'''
- #백트래킹 #조합

- k, *s
'''