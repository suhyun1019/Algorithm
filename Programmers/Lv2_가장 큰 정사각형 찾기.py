# dp
def solution(board):
    len_x, len_y = len(board[0]), len(board)
    dp=[[0 for _ in range(len_x)] for _ in range(len_y)]
    if len_x==1 or len_y==1 :
        return 1
    m = 0
    for i in range(len_y) :
        for j in range(len_x) :
            if i==0 or j==0 :
                dp[i][j] = board[i][j]
            elif board[i][j] :
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
                if dp[i][j]>m :
                    m = dp[i][j]
    return m**2
