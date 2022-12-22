n = int(input())

arr = [1e9] * 1000003
arr[1] = 0

for i in range(2, n+1):
    mn = arr[i-1] + 1
    if i%3 == 0:
        mn = min(mn, arr[i//3] + 1)
    if i%2 == 0:
        mn = min(mn, arr[i//2] + 1)
    arr[i] = mn

print(arr[n])

'''
- 3과 2를 elif로 구분하면 안됨. 둘다 나눠질 때는 모두 비교해야 하기 때문.
    - https://www.acmicpc.net/board/view/92152
'''