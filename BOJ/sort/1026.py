n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

print(sum([x*y for x,y in zip(a, b)]))

'''
- #그리디 #정렬

- sort reverse
- [x*y for x,y in zip(a, b)]
'''