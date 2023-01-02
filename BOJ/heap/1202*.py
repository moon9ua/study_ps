import heapq
import sys
input = sys.stdin.readline

n,k = map(int, input().split())
gem = [tuple(map(int, input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(k)]
gem.sort()
bag.sort()

heap = []
idx = 0
ret = 0
for b in bag:
    for i in range(idx, n):
        m,v = gem[i]
        if m > b:
            break
        heapq.heappush(heap, -v)
        idx += 1
    
    if heap:
        ret += -heapq.heappop(heap)

print(ret)

'''
- 알고리즘 참고: https://jaimemin.tistory.com/760
- gem도 heap으로 구현한 풀이들이 있는데, 나는 list&index를 사용해서 더 빠른 듯? 
- 틀렸던 풀이:
    for i in range(idx, n):
        idx = i
    i가 n-1인 경우, 다음 값이 갱신이 안돼서 계속 push되는 문제가 있었음.
    idx += 1로 수정하여 해결.
'''