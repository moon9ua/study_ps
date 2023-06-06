# 통과 테스트용 제출
import sys

input = sys.stdin.readline
INF = int(1e9)


# 벨만 포드 알고리즘 응용 -> 그래프상 음의 싸이클 존재 판단 함수
def bf(start):
    dis = [INF] * (n+1)  # 최단거리 초기화
    dis[start]=0
    # 메인 로직
    # 음의 사이클 판별을 위해 n번 반복
    for i in range(n):
        # 반복마다 모든 간선 확인
        for edge in edges:
            cur = edge[0] # 출발
            next_node = edge[1] # 도착
            cost = edge[2] # 비용

            
            # 다음 노드로 이동하는 거리가 최단거리로 갱신가능한 경우
            if dis[next_node] > cost + dis[cur]:
                dis[next_node] = cost + dis[cur]
                # i==n-1이면 n번 돌린건데 이때도 갱신이 발생하면 음의 싸이클 존재
                if i == n - 1:
                    return True

    return False


t = int(input())

for _ in range(t):
    # 지점수, 도로수, 웜홀수
    n, m, w = map(int, input().split())
    edges = []

    # 도로 정보
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    # 웜홀 정보
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    # bf알고리즘 조건에 dis[cur]!=INF 조건이 없으므로
    # 시작 위치는 아무거나 무관
    # bf는 최단거리 알고리즘이 아닌 음의 싸이클의 판별 유무 판단 알고리즘
    key = bf(1)
    if key:
        print("YES")
    else:
        print("NO")
