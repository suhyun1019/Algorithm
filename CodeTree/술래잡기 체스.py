"""
시작: 2:46
종료: 5:19
"""

inputs = [list(map(int, input().split())) for _ in range(4)]
moves = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
horse_pos = {}  # 최종 번호, 방향 
board = [[0 for _ in range(4)] for _ in range(4)]   # 말의 위치(술래:-1)
res = []

for i in range(4):
    for j in range(4):
        horse_pos[inputs[i][2*j]]=[i,j,(inputs[i][2*j+1]-1)%8]
        board[i][j]=inputs[i][2*j]
horse_pos = dict(sorted(horse_pos.items(), key=lambda x:x[0]))

def moving(board, horse_pos):

    for num, pos in horse_pos.items():
        if pos==-1:
            continue
        x,y,d = pos[0],pos[1],pos[2]
        cnt = 0
        while cnt<8:
            dx,dy = x+moves[d][0],y+moves[d][1]
            if 0<=dx<4 and 0<=dy<4 and board[dx][dy]>=0: # 술래:-1, 없으면:0
                if board[dx][dy]==0:
                    board[dx][dy] = num
                    board[x][y] = 0
                    horse_pos[num] = [dx,dy,d]
                else:
                    changed_num = board[dx][dy]
                    changed_d = horse_pos[changed_num][2]
                    board[dx][dy],board[x][y] = board[x][y], board[dx][dy]
                    horse_pos[num] = [dx,dy,d]
                    horse_pos[changed_num] = [x,y,changed_d]
                break
            else:
                d = (d+1)%8
                cnt+=1
    
    return  

def dfs(x,y,d,score, board, horse_pos):
    
    board_copy = [b[:] for b in board]
    horse_pos_copy = horse_pos.copy()

    moving(board_copy, horse_pos_copy)

    for i in range(1,4):
        dx,dy = x+moves[d][0]*i,y+moves[d][1]*i
        if 0<=dx<4 and 0<=dy<4 and board_copy[dx][dy]>0:
            now = board_copy[dx][dy]
            temp = horse_pos_copy[now]
            changed_d = horse_pos_copy[now][2]
            horse_pos_copy[now] = -1 # 말이 잡힘 
            board_copy[dx][dy] = -1
            board_copy[x][y] = 0
            dfs(dx,dy,changed_d,score+now, board_copy, horse_pos_copy)
            board_copy[x][y] = -1
            board_copy[dx][dy] = now
            horse_pos_copy[now] = temp

    res.append(score)

s_num = board[0][0]
d = horse_pos[s_num][2]
horse_pos[s_num] = -1   # 해당 말은 잡힘
board[0][0] = -1        # 술래 들어감 
board_copy = [b[:] for b in board]
horse_pos_copy = horse_pos.copy()
dfs(0,0,d,s_num, board_copy, horse_pos_copy)
print(max(res))
