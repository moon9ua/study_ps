import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))

op_list = ['+', '-', '*', '//']
mx = -1e9
mn = 1e9

def func(k, ret):
    global mx, mn

    if k == len(nums)-1:
        mx = max(mx, ret)
        mn = min(mn, ret)
        return
    
    for i in range(4):
        if op[i]:
            op[i] -= 1
            if i == 3 and ret < 0:
                func(k+1, -(-ret//nums[k+1])) # C++14 나눗셈 기준
            else:
                func(k+1, eval(str(ret)+op_list[i]+str(nums[k+1])))
            op[i] += 1

func(0, nums[0])
print(mx, mn)

'''
- 제목: 연산자 끼워넣기
- 난이도: 실버 1
- 제출: 1
- 분류: 재귀, 백트래킹, 완전탐색

- 테케가 잘 되어 있어, 테케만 점검하여 바로 통과
'''