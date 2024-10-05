n,l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

def find(board):
    cnt = 0
    for i in range(n):
        now = [board[i][0],0] # 현재 높이, 지속 기간  
        flag = 0
        for j in range(n):
            if now[0]>board[i][j]:
                if now[0]-board[i][j]>1:
                    break
                t = 1
                while j+t<n and board[i][j]==board[i][j+t] and t<l:
                    t+=1
                if t>=l:
                    now = [board[i][j], t*(-1)+1]
                else:
                    break
            elif now[0]<board[i][j]:
                if board[i][j]-now[0]>1:
                    break
                if now[1]>=l:
                    now = [board[i][j], 1]
                else:
                    break
            elif now[0]==board[i][j]: # 높이 같음
                now[1]+=1
                
            if j==n-1:
                flag = 1
        if flag:
            cnt+=1
    return cnt

rotate_board = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        rotate_board[i][j]=board[j][i]

cnt+=find(board)
cnt+=find(rotate_board)
print(cnt)
