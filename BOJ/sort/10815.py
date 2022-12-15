import sys
input = sys.stdin.readline

pos = [0] * 10000003
neg = [0] * 10000003

n = int(input())
for num in map(int, input().split()):
    if num >= 0:
        pos[num] = 1
    else:
        neg[-num] = 1

m = int(input())
for num in map(int, input().split()):
    if num >= 0:
        print(pos[num], end=' ')
    else:
        print(neg[-num], end=' ')

'''
- #배열_활용
- 시간복잡도: O(N+M) = O(1,000,000)

- print end
- 10,000,000 길이 리스트는 약 40MB?
'''