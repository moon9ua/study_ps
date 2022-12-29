import sys
input = sys.stdin.readline

n,c = map(int, input().split())
homes = [int(input()) for _ in range(n)]
homes.sort()

l, r = 0, max(homes)-min(homes)
ret = 0

while l <= r:
    mid = (l+r)//2
    router = 1
    prev = 0

    for i in range(1, n):
        if homes[i] - homes[prev] >= mid:
            router += 1
            prev = i

    if router >= c:
        l = mid + 1
        ret = mid
    else:
        r = mid - 1

print(ret)

'''
- ret 대신 r을 그냥 출력해도 된다. (https://www.acmicpc.net/board/view/92735)
- 범위는 좁게만 아니면 넓게는 상관 없는 듯? (ex. r=max(homes)+100)
'''