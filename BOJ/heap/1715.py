import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = [int(input()) for _ in range(n)]
heapq.heapify(heap)
ret = 0

while len(heap) > 1:
    s = heapq.heappop(heap) + heapq.heappop(heap)
    heapq.heappush(heap, s)
    ret += s

print(ret)

'''
- "힙 & 그리디" 문제인걸 아는게 관건.
- 리스트 -> 힙
- 오답
    - `heap = [int(input()) for _ in range(n)]` : heap은 heappush하거나 heapify해야한다.
    - `heap = heapq.heapify([...])` : heapify는 리턴이 아니라 제자리 변환.
'''