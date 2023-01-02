import heapq
import sys
input = sys.stdin.readline

n = int(input())
lheap = []
rheap = []

for _ in range(n):
    x = int(input())

    if len(lheap) == len(rheap):
        heapq.heappush(lheap, (-x,x))
    else:
        heapq.heappush(rheap, (x,x))

    if rheap and lheap[0][1] > rheap[0][1]:
        l = heapq.heappop(lheap)[1]
        r = heapq.heappop(rheap)[1]
        heapq.heappush(rheap, (l,l))
        heapq.heappush(lheap, (-r,r))

    print(lheap[0][1])

'''
- 최대힙: 부호 일일이 계산하지 않고, (-x,x) (x,x)로 넣어주고 1번째 항 쓰는게 편리.
'''