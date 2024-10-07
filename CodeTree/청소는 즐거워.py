"""
시작: 4:05
종료: 5:28

실수
- 설계를 체계적으로 하니 딱히 없었음
"""

pos_left = {1:[(-1,1),(1,1)], 2:[(-2,0),(2,0)], 5:[(0,-2)], 7:[(-1,0),(1,0)], 10:[(-1,-1),(1,-1)], 0:(0,-1)}
pos_down = {1:[(-1,-1),(-1,1)], 2:[(0,2),(0,-2)], 5:[(2,0)], 7:[(0,1),(0,-1)], 10:[(1,1),(1,-1)], 0:(1,0)}
pos_right = {1:[(-1,-1),(1,-1)], 2:[(-2,0),(2,0)], 5:[(0,2)], 7:[(-1,0),(1,0)], 10:[(1,1),(-1,1)], 0:(0,1)}
pos_up = {1:[(1,-1),(1,1)], 2:[(0,2),(0,-2)], 5:[(-2,0)], 7:[(0,1),(0,-1)], 10:[(-1,-1),(-1,1)], 0:(-1,0)}
moves = [(0,-1),(1,0),(0,1),(-1,0)] # left,down,right,up
dust_num = [2,2,1,2,2]
dic = {1:0, 2:1, 5:2, 7:3, 10:4}
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
global rest_dust
rest_dust = 0

def dust_move(x,y,d):
    global rest_dust

    total = board[x][y]
    board[x][y] = 0
    dust_list = cal_dust(total) #1,2,5,7,10
    temp_sum = 0

    if d==0:
        pos = pos_left
    elif d==1:
        pos = pos_down
    elif d==2:
        pos = pos_right
    elif d==3:
        pos = pos_up
    
    for k,po in pos.items():
        if k!=0:
            for mx,my in po:
                dx,dy = x+mx,y+my
                if 0<=dx<n and 0<=dy<n:
                    board[dx][dy]+=dust_list[dic[k]]
                else:
                    rest_dust+=dust_list[dic[k]]
                temp_sum+=dust_list[dic[k]]

    # 앞에 남은 먼지 더하기       
    rest = total-temp_sum
    ax,ay = x+pos[0][0],y+pos[0][1]
    if 0<=ax<n and 0<=ay<n:
        board[ax][ay]+=rest
    else:
        rest_dust+=rest

# 먼지 양 계산
def cal_dust(total):

    dust_list = [0,0,0,0,0] #1,2,5,7,10
    ratio = [0.01, 0.02, 0.05, 0.07, 0.1]
    for i in range(5):
        dust_list[i] = int(total*ratio[i])
    return dust_list

x,y,d = n//2, n//2, 0
cnt = 0
flag= 1
while flag:
    for i in range(cnt//2+1):
        x+=moves[d][0]
        y+=moves[d][1]
        dust_move(x,y,d)
        if x==0 and y==0:
            flag = 0
            break
    d = (d+1)%4
    cnt+=1

print(rest_dust)
