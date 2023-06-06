import sys
input = sys.stdin.readline

def bf(st):
    dist[st] = 0
    for i in range(N):
        for edge in edges:
            cur, nxt, cost = edge
            # if dist[cur] != 1e9 and dist[nxt] > dist[cur] + cost:
            if dist[nxt] > dist[cur] + cost:
                dist[nxt] = dist[cur] + cost
                if i == N-1:
                    return True # 음수 사이클 존재
    return False

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    dist = [1e9] * (N+1)
    edges = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
        edges.append((b, a, c))
    for _ in range(W):
        a, b, c = map(int, input().split())
        edges.append((a, b, -c))

    neg_cycle = bf(1)
    print('YES' if neg_cycle else 'NO')