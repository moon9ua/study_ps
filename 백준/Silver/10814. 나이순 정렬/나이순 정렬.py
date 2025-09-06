import sys

input = sys.stdin.readline

n = int(input())

lst = []

for i in range(n):
    age, name = input().split()
    lst.append((int(age), name, i))

sorted_lst = sorted(lst, key=lambda x: (x[0], x[2]))

for x in sorted_lst:
    print(x[0], x[1])
