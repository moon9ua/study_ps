import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)

def func():
    n = int(input())
    stu = [0] + list(map(int, input().split()))
    vis = [False] * (n+1)
    cnt = n

    def dfs(curr):
        nonlocal cnt
        vis[curr] = True
        road.append(curr)
        nxt = stu[curr]

        if vis[nxt]:
            if nxt in road:
                teamed = len(road) - road.index(nxt)
                cnt -= teamed
            return

        dfs(nxt)

    for i in range(1, n+1):
        if not vis[i]:
            road = []
            dfs(i)

    print(cnt)

t = int(input())
for _ in range(t):
    func()