from collections import deque, defaultdict
import sys
input = sys.stdin.readline

case = 1
while True:
    n,m = map(int, input().split())
    if n == 0:
        break
    graph = defaultdict(list)
    for _ in range(m):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    p = [0] * (n+1)

    def bfs(cur):
        q = deque()
        q.append(cur)
        ret = 1
        while q:
            x = q.popleft()
            for nx in graph[x]:
                if p[x] == nx:
                    continue
                if p[nx] != 0:
                    ret = 0
                    continue
                p[nx] = x
                q.append(nx)
        return ret

    ans = 0
    for i in range(1, n+1):
        if p[i] == 0:
            ans += bfs(i)

    print(f'Case {case}: ', end='')
    if ans == 0:
        print('No trees.')
    elif ans == 1:
        print('There is one tree.')
    else:
        print(f'A forest of {ans} trees.')

    case += 1