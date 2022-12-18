import sys
input = sys.stdin.readline

n = int(input())
plus = [0] * 10000003
minus = [0] * 10000003

for num in map(int, input().split()):
    if num >= 0:
        plus[num] += 1
    else:
        minus[-num] += 1

m = int(input())

for num in map(int, input().split()):
    if num >= 0:
        print(plus[num], end=' ')
    else:
        print(minus[-num], end=' ')

'''
- #카운팅_정렬
- 233044KB, 948ms
'''