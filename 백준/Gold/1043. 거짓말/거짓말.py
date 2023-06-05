import sys
input = sys.stdin.readline

n, m = map(int, input().split())
_, *truth = list(map(int, input().split()))

know_truth = 0
p = [i for i in range(n+1)]
for person in truth:
    p[person] = know_truth

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        p[b] = a
    else:
        p[a] = b

parties = []
for _ in range(m):
    k, *party = list(map(int, input().split()))
    parties.append(party)
    for i in range(k-1):
        union(party[i], party[i+1])

cnt = 0
for party in parties:
    tmp = 1
    for person in party:
        if find(person) == know_truth:
            tmp = 0
            break
    cnt += tmp

print(cnt)