n = int(input())
table = [list(map(int, input().split())) for _ in range(n*n)]
ans = [[0]*n for _ in range(n)] # 학생들이 앉는 자리 
move = [(1,0),(0,1),(-1,0),(0,-1)]
dic = {}

for i,t in enumerate(table):
    dic[t[0]] = t[1:]
    table[i] = t[0]

# 최적의 자리 찾기: 좋아하는 친구-비어있는간-행-
def find_seat(k):
    temp = []

    for i in range(n):
        for j in range(n):
            if ans[i][j]==0: #빈자리에서만 탐색가능
                t = [0,0,i,j] # 좋아하는 친구수, 빈자리, 좌표
                for m in move:
                    dx,dy = i+m[0],j+m[1]
                    if 0<=dx<n and 0<=dy<n:
                        if ans[dx][dy]==0:
                            t[1]+=1
                        elif ans[dx][dy] in dic[k]:
                            t[0]+=1
                temp.append(t)
    temp.sort(key=lambda x:(-x[0],-x[1],x[2],x[3]))
    ans[temp[0][2]][temp[0][3]] = k
    return

for t in table:
    find_seat(t)

s = [0]*(n*n)
for i in range(n):
    for j in range(n):
        for m in move:
            dx,dy = i+m[0],j+m[1]
            if 0<=dx<n and 0<=dy<n and ans[dx][dy] in dic[ans[i][j]]:
                s[ans[i][j]-1]+=1
        if s[ans[i][j]-1]>0:
            s[ans[i][j]-1] = 10**(s[ans[i][j]-1]-1)
print(sum(s))
