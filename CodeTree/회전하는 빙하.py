from collections import deque

# 회전시키기 : 시작 좌표, 변수 길이 
def rotate(x, y, level):
    
    k = 2**(level-1) # 한칸의 길이
    end = 2**level   # 총 길이(끝)
    
    t1 = [[table[x+i][y+j] for j in range(k)] for i in range(k)]
    t2 = [[table[x+i][y+j] for j in range(k, end)] for i in range(k)]
    t3 = [[table[x+i][y+j] for j in range(k)] for i in range(k, end)]
    t4 = [[table[x+i][y+j] for j in range(k, end)] for i in range(k, end)]
    
    for i in range(end):
        for j in range(end):
            if i<k:
                if j<k:
                    table[x+i][y+j]=t3[i][j]
                else:
                    table[x+i][y+j]=t1[i][j-k]
            else:
                if j<k:
                    table[x+i][y+j]=t4[i-k][j]
                else:
                    table[x+i][y+j]=t2[i-k][j-k]

    return

# 얼음 녹음
def malt():

    malt_list = []
    for i in range(nn):
        for j in range(nn):
            cnt = 0
            for m in move:
                dx,dy = i+m[0],j+m[1]
                if 0<=dx<nn and 0<=dy<nn and table[dx][dy]>0:
                    cnt+=1
            if cnt<3:
                malt_list.append((i,j))
    for ml in malt_list:
        if table[ml[0]][ml[1]]>0:
            table[ml[0]][ml[1]]-=1

# 얼음군 찾기
def bfs(x,y):

    q = deque()
    q.append((x,y))
    table[x][y]=0
    cnt = 1

    while q:
        v = q.popleft()
        for m in move:
            dx,dy = v[0]+m[0], v[1]+m[1]
            if 0<=dx<nn and 0<=dy<nn and table[dx][dy]>0:
                table[dx][dy]=0
                q.append((dx,dy))
                cnt+=1
    return cnt

n,q = map(int, input().split())
nn = 2**n
table = [list(map(int, input().split())) for _ in range(nn)]
rotate_level = list(map(int, input().split()))
move = [(1,0),(0,1),(-1,0),(0,-1)]

for level in rotate_level:
    if level>0:
        k = 2**level
        for i in range(0, nn, k):
            for j in range(0, nn, k):
                rotate(i, j, level)
    malt()

s, v = 0, 0
for i in range(nn):
    s+=sum(table[i])
print(s)

for i in range(nn):
    for j in range(nn):
        if table[i][j]>0:
            v = max(bfs(i,j), v)
print(v)
