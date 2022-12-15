n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()
print(*nums, sep='\n') # *, sep

'''
- #정렬
- 시간복잡도: O(NlogN), N = 1000

- print sep
'''