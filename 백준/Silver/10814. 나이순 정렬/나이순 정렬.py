n = int(input())

lst = []

for i in range(n):
    age, name = input().split()
    lst.append((int(age), name, i))

lst.sort(key=lambda x: (x[0], x[2]))

for x in lst:
    print(x[0], x[1])
