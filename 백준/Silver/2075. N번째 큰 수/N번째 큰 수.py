import heapq
import sys
input = sys.stdin.readline

n = int(input())
pq = []
for _ in range(n):
    for item in map(int, input().split()):
        heapq.heappush(pq, item)
        if len(pq) > n:
            heapq.heappop(pq)

print(heapq.heappop(pq))