import sys
sys.setrecursionlimit(1000000)

def dfs(x, y, cnt, board, dp) :
    
    global answer
    
    if board[x][y]=='G' :
        answer = min(answer, cnt)
        return
    elif dp[x][y] and dp[x][y]<=cnt:
        return
    
    dp[x][y]=cnt
    
    i,j = x,y
    while i<len(board)-1 and board[i+1][j]!='D' :
        i+=1
    dfs(i, j, cnt+1, board, dp)
    
    i,j = x,y
    while j<len(board[0])-1 and board[i][j+1]!='D' :
        j+=1
    dfs(i, j, cnt+1, board, dp)
    
    i,j = x,y
    while i>0 and board[i-1][j]!='D' :
        i-=1
    dfs(i, j, cnt+1, board, dp)
    
    i,j = x,y
    while j>0 and board[i][j-1]!='D' :
        j-=1
    dfs(i, j, cnt+1, board, dp)
    
    return

def solution(board):
    global answer
    answer = 1000
    dp = [[0 for j in range(len(board[0]))] for i in range(len(board))]
    
    for i in range(len(board)) :
        for j in range(len(board[0])) :
            if board[i][j]=='R' :
                dfs(i,j,0, board, dp)
                break
    return answer if answer!=1000 else -1
