n = int(input())

x = 1
cnt = 0

for i in range(1, n+1):
    x *= i
    while x % 10 == 0:
        x = x // 10
        cnt += 1

print(cnt)