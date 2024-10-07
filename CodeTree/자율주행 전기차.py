"""
시작: 9:55
종료: 11:50
"""
from collections import deque

n,m,c = map(int, input().split()) # 격자, 승객, 배터리 
board = [list(map(int, input().split())) for _ in range(n)]
init_pos = list(map(int, input().split()))
destination = [list(map(int, input().split())) for _ in range(m)]
des_dic = {}    # 승객의 도착지 정보 저장 
moves = [(-1,0),(0,-1),(0,1),(1,0)]

for i in range(n):
    for j in range(n):
        if board[i][j]==1:  # 벽 -1
            board[i][j] = -1

for i,des in enumerate(destination):
    s,e = des[0]-1,des[1]-1
    board[s][e] = i+1
    des_dic[i+1] = [des[0]-1,des[1]-1,des[2]-1,des[3]-1]


# 번호, 깊이
def bfs(s,e):
    res = []
    q = deque()
    q.append((s,e,0)) #위치, 깊이
    visited = [(s,e)]
    found = 1   # 손님 못찾음
    depth = 1
    fix_depth = 400

    if board[s][e]>0:
        temp = board[s][e]
        board[s][e] = 0
        return [temp, 0]

    while q:
        v = q.popleft()
        for mx,my in moves:
            dx,dy = v[0]+mx,v[1]+my
            if 0<=dx<n and 0<=dy<n and board[dx][dy]>=0 and (dx,dy) not in visited:
                if v[2]+1<=fix_depth:
                    visited.append((dx,dy))
                    q.append((dx,dy,v[2]+1))
                if board[dx][dy]>0 and v[2]+1<=fix_depth:  # 최단 거리 손님 발견
                    fix_depth = v[2]+1
                    res.append([dx,dy,v[2]+1])
        depth+=1

    if res:
        res.sort(key=lambda x:(x[0],x[1]))
        ans = res[0]
        temp = board[ans[0]][ans[1]]
        board[ans[0]][ans[1]] = 0
        return [temp, ans[2]]
    else:
        return [-1,-1]

def check(s_x,s_y,e_x,e_y):

    q = deque()
    q.append((s_x,s_y,0))
    visited = [(s_x,s_y)]
    while q:
        v = q.popleft()
        if v[0]==e_x and v[1]==e_y:
            return v[2]
        for mx,my in moves:
            dx,dy = v[0]+mx,v[1]+my
            if 0<=dx<n and 0<=dy<n and board[dx][dy]>=0 and (dx,dy) not in visited:
                visited.append((dx,dy))
                q.append((dx,dy,v[2]+1))
    return -1

def cal(x, y, total):
    
    # 가까운 손님, 거리 계산
    res = bfs(x,y)
    num,moving = res[0],res[1]
    
    if num==-1 and moving==-1:
        for i in range(n):
            for j in range(n):
                if board[i][j]>0:
                    return -1
        return total
    
    if total<moving:
        return -1
    
    total -= moving
    s_x,s_y,e_x,e_y = des_dic[num][0],des_dic[num][1],des_dic[num][2],des_dic[num][3]
    distance = check(s_x,s_y,e_x,e_y)

    if distance==-1:
        return -1

    if total>=distance:
        total = total+distance
    else:
        return -1
    
    return cal(e_x,e_y,total)

t = cal(init_pos[0]-1,init_pos[1]-1,c)
print(t)
