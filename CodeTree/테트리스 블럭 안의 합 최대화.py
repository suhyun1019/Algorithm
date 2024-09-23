def dfs(x, y, s, visited) :
    global answer, start_x, start_y
    
    if len(visited)==4 :
        answer = max(answer, s)
        return

    for d in direction :
        dx, dy = x+d[0], y+d[1]
        if 0<=dx<n and 0<=dy<m and (dx, dy) not in visited :
            visited.append((dx, dy))
            dfs(dx, dy, s+table[dx][dy], visited)
            visited.pop()
        elif dx==start_x and dy==start_y :
            dfs(dx, dy, s, visited)

n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
global answer, start_x, start_y
answer = 0
direction=[(1,0),(0,1),(-1,0),(0,-1)]

for i in range(n) :
    for j in range(m) :
        start_x, start_y = i, j
        dfs(i, j, table[i][j], [(i,j)])

print(answer)
