n,m = map(int, input().split())
trees = [list(map(int, input().split())) for _ in range(n)]
years = [list(map(int, input().split())) for _ in range(m)]
direct = [(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1)]

def move(d, m, table):  # 방향,크기,영양제 구역
    new = []
    for t in table:
        dx,dy = (t[0]+direct[d][0]*m)%(n),(t[1]+direct[d][1]*m)%(n)
        new.append((dx,dy))
        trees[dx][dy]+=1
    return new

def check(table):
    new = []
    for i in range(len(table)):
        for di in range(1, len(direct), 2): # 1,3,5,7
            dx,dy = table[i][0]+direct[di][0],table[i][1]+direct[di][1]
            if 0<=dx<n and 0<=dy<n and trees[dx][dy]>0:
                trees[table[i][0]][table[i][1]]+=1

    for i in range(n):
        for j in range(n):
            if trees[i][j]>=2 and (i,j) not in table:
                trees[i][j]-=2
                new.append((i,j))
    return new

vi = [(n-2,0),(n-2,1),(n-1,0),(n-1,1)]
for year in years:
    vi = move(year[0]-1, year[1], vi)
    vi = check(vi)

s = 0
for i in range(n):
    s+=sum(trees[i])
print(s)
