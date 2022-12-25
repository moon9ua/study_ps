import sys
input = sys.stdin.readline

n = int(input())
cost = [0] + list(map(int, input().split()))

arr = cost[:]

for i in range(1, n+1):
    for j in range(1, i):
        arr[i] = max(arr[i], arr[i-j] + cost[j])

print(arr[n])

'''
- 이중 반복문 dp
- 리스트 깊은복사
'''