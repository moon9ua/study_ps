import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ns = set(input().rstrip() for _ in range(n))
ms = set(input().rstrip() for _ in range(m))

ans = ns & ms
print(len(ans))
print(*sorted(ans), sep='\n')