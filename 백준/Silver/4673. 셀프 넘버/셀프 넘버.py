dp = [True] * 10005

for i in range(1, 10001):
    curr = i
    while True:
        nxt = i + sum(map(int, str(i)))
        if not (nxt <= 10000 and dp[nxt]):
            break
        dp[nxt] = False
        curr = nxt

for i in range(1, 10001):
    if dp[i]:
        print(i)