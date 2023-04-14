from collections import defaultdict
import sys
input = sys.stdin.readline

k,l = map(int,input().split())
hash = defaultdict(int)

student = []
for i in range(l):
    a = input().rstrip()
    hash[a] = i
    student.append(a)

cnt = 0
for i in range(l):
    if hash[student[i]] == i:
        print(student[i])
        cnt += 1
    if cnt == k:
        break