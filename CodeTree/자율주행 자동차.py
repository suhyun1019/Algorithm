def dfs(x, y, visited, board, d) :
    
    cnt=0 # 4방향 다 돌았는지 확인
    while cnt<4 :
        dx,dy = x+direction[(d-1)%4][0], y+direction[(d-1)%4][1]
        if 0<=dx<n and 0<=dy<m and board[dx][dy]==0 and (dx,dy) not in visited :
            visited.append((dx, dy))
            visited = dfs(dx, dy, visited, board, (d-1)%4)
            return visited
        d=(d-1)%4
        cnt+=1
    
    dx,dy = x+direction[(d-2)%4][0], y+direction[(d-2)%4][1]
    if 0<=dx<n and 0<=dy<m and board[dx][dy]==0 :
        visited = dfs(dx, dy, visited, board, d)
    return visited


n,m = map(int, input().split())
x,y,d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

direction = [[-1,0],[0,1],[1,0],[0,-1]]
visited = [(x,y)]

v = dfs(x, y, visited, board, d)
print(len(v))
