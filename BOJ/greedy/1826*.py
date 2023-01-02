import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)] # n
l,p = map(int, input().split())

arr.append([l, 0])
arr.sort()

rest = p
prev = 0
oil = []
ret = 0
for a,b in arr:
    rest -= a-prev
    while rest < 0 and oil:
        rest += -heapq.heappop(oil)
        ret += 1
    if rest < 0:
        print(-1)
        exit()
    if a == l:
        break
    heapq.heappush(oil, -b)
    prev = a

print(ret)

'''
- 13305를 안풀었다면 아이디어가 생각이 안났을 듯.
'''