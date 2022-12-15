import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * 10005
for _ in range(n):
    x = int(input())
    arr[x] += 1
    
for num in range(1, 10001):
    for _ in range(arr[num]):
        print(num)

'''
- #카운팅_정렬
- 시간복잡도: O(N), N = 10,000,000
'''