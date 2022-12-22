import sys
input = sys.stdin.readline

n = int(input())
score = [int(input()) for _ in range(n)]

if n == 1:
    print(score[0])
    exit()

arr = [[0] * n for _ in range(2)]
arr[0][0] = score[0]
arr[0][1] = score[1]
arr[1][1] = score[0] + score[1]

for i in range(2, n):
    arr[0][i] = max(arr[0][i-2], arr[1][i-2]) + score[i]
    arr[1][i] = arr[0][i-1] + score[i]

print(max(arr[0][n-1], arr[1][n-1]))

'''
- 초기값이 불가능한 경우는 반드시 얼리리턴 해야한다.
'''