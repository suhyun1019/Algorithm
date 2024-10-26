def solution(n):
    global answer
    answer = 0
    board = [[0]*n for _ in range(n)]
    
    # 해당 부분 a -> b
    def check(x,y,a,b):
        moves = [(1,0),(0,1),(0,-1),(1,1),(1,-1)]
        
        for mx,my in moves:
            dx,dy = x,y
            while 0<=dx<n and 0<=dy<n:
                if board[dx][dy]==a:
                    board[dx][dy]=b
                dx+=mx
                dy+=my
        return
    
    def dfs(x):
        global answer
        
        if x>=n:
            answer+=1
            return
        
        for i in range(x, n):
            for j in range(n):
                if board[i][j]==0:
                    check(i,j,0,i+1)
                    dfs(i+1)
                    check(i,j,i+1,0)
            else:
                return
        return

    dfs(0)
    return answer
