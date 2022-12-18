from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
card.sort()

m = int(input())
for num in map(int, input().split()):
    ret = bisect_right(card, num) - bisect_left(card, num)
    print(ret, end=' ')

'''
- #이진탐색
- 99300KB, 1556ms

- N=500000, M=500000
- 시간복잡도: O(NlogN + MlogN)
'''