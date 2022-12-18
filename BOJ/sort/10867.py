import sys
input = sys.stdin.readline

n = int(input())
s = set(map(int, input().split()))

print(*sorted(list(s)))

'''
- set map
- set list로 변환하여 정렬
'''