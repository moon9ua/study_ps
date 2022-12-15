import sys
input = sys.stdin.readline # 안하면 시간초과

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()
print(*nums, sep='\n')

'''
- #정렬
- 시간복잡도: O(NlogN), N = 1,000,000

- sys.stdin.readline
'''