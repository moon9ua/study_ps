def solution(m, n, puddles):
    board = [[1] * n for _ in range(m)] # (x, y) == board[m][n] == [[0]*n for _ in range(m)] 을 기억!
    for (x, y) in puddles:
        board[x-1][y-1] = 0
        
    for i in range(0, m): # 1부터 시작하면 가장자리 우물을 반영하지 못한다.
        for j in range(0, n):
            if (i == 0 and j == 0) or board[i][j] == 0: # 우물일 때는 스킵
                continue
            elif i == 0:
                board[i][j] = board[i][j-1] % 1000000007 # 나머지 연산 빼먹으면 효율성 탈락
            elif j == 0:
                board[i][j] = board[i-1][j] % 1000000007
            else:
                board[i][j] = (board[i-1][j] + board[i][j-1]) % 1000000007
    
    return board[m-1][n-1]