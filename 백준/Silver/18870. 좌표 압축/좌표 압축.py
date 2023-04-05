from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))

nx = sorted(x)
arr = [nx[0]]
for i in range(1, len(nx)):
    if nx[i] != nx[i-1]:
        arr.append(nx[i])

for xi in x:
    print(bisect_left(arr, xi), end=' ')