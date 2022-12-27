import sys
input = sys.stdin.readline

k = int(input())
ins = input().rstrip().split()

vis = [False] * 10
mx = 0
mn = '9' * (k+1)

def func(idx):
    global mx, mn

    if idx == k+1:
        s = ''.join(map(str, ret))
        if int(mx) < int(s):
            mx = s
        if int(mn) > int(s):
            mn = s
        return

    for i in range(10):
        if vis[i]:
            continue
        if ret and ins[idx-1] == '<' and not ret[-1] < i:
            continue
        if ret and ins[idx-1] == '>' and not ret[-1] > i:
            continue
            
        vis[i] = True
        ret.append(i)
        func(idx+1)
        vis[i] = False
        ret.pop()

ret = []
func(0)

print(mx)
print(mn)

'''
- n=10(k=9)이므로 팩토리얼 시간복잡도가 가능하여 백트래킹으로 풀어보았다.
- '9' * (k+1): mn 초기값에 유의
- if ret and ins[idx-1] == '<' and not ret[-1] < i
- BOJ 길라잡이에서 그리디로 분류되어 있는데, 왜? 어떻게?
'''