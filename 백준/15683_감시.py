n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
move = [(1,0),(0,1),(-1,0),(0,-1)]
# 번호마다 움직이는 조합
dic = {1:[[0],[1],[2],[3]], 2:[[0,2],[1,3]], 3:[[0,1],[1,2],[2,3],[3,0]], 4:[[0,1,2],[1,2,3],[2,3,0],[3,0,1]], 5:[[0,1,2,3]]}
global ans
ans = 0

def dfs(cctv_list, idx, visited):
    global ans

    if len(cctv_list)==idx:
        ans = max(ans, len(visited))
        return

    v = cctv_list[idx]
    x,y,cctv_num = v[0],v[1],v[2]
    if (x,y) not in visited:
        visited.append((x,y))

    for cctv in dic[cctv_num]:
        #temp = copy.deepcopy(visited)
        temp = [v[:] for v in visited]
        for ci in range(len(cctv)):
            c = cctv[ci]
            dx,dy = x+move[c][0],y+move[c][1]
            while 0<=dx<n and 0<=dy<m and board[dx][dy]<6:
                if (dx,dy) not in temp:
                    temp.append((dx,dy))
                dx+=move[c][0]
                dy+=move[c][1]
        dfs(cctv_list, idx+1, temp)
        #visited = copy.deepcopy(temp)

total = 0
cctv_list = []  # 좌표, 번호
for i in range(n):
    for j in range(m):
        if 1<=board[i][j]<=5:
            cctv_list.append((i,j,board[i][j]))
        if board[i][j]<6:
            total+=1
dfs(cctv_list, 0, [])
print(total-ans)
