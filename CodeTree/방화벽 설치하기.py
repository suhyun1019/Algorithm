#from collections import deque

n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
wall_num = 0
ground = []
comb = []
moves = [(1,0),(0,1),(-1,0),(0,-1)]
fire = []

for i in range(n):
    for j in range(m):
        if board[i][j]==1:
            wall_num+=1
        elif board[i][j]==0:
            ground.append((i,j))
        else:
            fire.append((i,j))

# 방화벽 3개 모든 조합 구하기 
def combination():

    for i in range(len(ground)-2):
        for j in range(i+1, len(ground)-1):
            for k in range(j+1, len(ground)):
                comb.append((ground[i],ground[j],ground[k]))

# 불 번짐 
def fire_area(x, y, board):

    q = []
    q.append((x,y))
    cnt = 1
    board[x][y]=-1

    while q:
        v = q.pop(0)
        for move in moves:
            dx,dy = v[0]+move[0],v[1]+move[1]
            if 0<=dx<n and 0<=dy<m and board[dx][dy]!=1 and board[dx][dy]!=-1:
                board[dx][dy]=-1
                cnt+=1
                q.append((dx,dy))
    
    return cnt

combination()
ans = n*m

for com in comb:
    board_copy = [b[:] for b in board]
    fire_cnt = 0
    for c in com:
        board_copy[c[0]][c[1]]=1
    for f in fire:
        if board_copy[f[0]][f[1]]!=-1:
            fire_cnt += fire_area(f[0], f[1], board_copy)
    ans = min(ans, fire_cnt)
print(n*m-ans-wall_num-3)방화벽 설치하기
