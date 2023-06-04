import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))

sorted_p = sorted(p)

acc = 0
ans = 0
for time in sorted_p:
    acc += time
    ans += acc

print(ans)