import sys
input = sys.stdin.readline

n = int(input())
s = {input().rstrip() for _ in range(n)}
lst = sorted(s, key=lambda x: [len(x), x])

print(*lst, sep='\n')

'''
- #정렬

- set 컴프리헨션
- set 리스트로 변환하여 정렬
- [len(x), x]
    - len(x)만 기준으로 삼으면 같은 길이끼리 정렬 기준이 없어 오답
'''