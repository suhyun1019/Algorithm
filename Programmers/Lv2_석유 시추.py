import sys
sys.setrecursionlimit(1000000)

def dfs(x, y, visited, land) :
    
    move = [(1,0),(0,1),(-1,0),(0,-1)]
    
    for i in range(4) :
        dx, dy = x+move[i][0], y+move[i][1]
        if 0<=dx<len(land) and 0<=dy<len(land[0]) :
            if land[dx][dy]==1 :
                land[dx][dy]=0
                visited.append(dy)
                visited = dfs(dx, dy, visited, land)
    return visited

def solution(land):
    answer = [0]*len(land[0])
    
    for i in range(len(land)) :
        for j in range(len(land[0])) :
            if land[i][j]==1 :
                land[i][j]=0
                visited = dfs(i, j, [j], land)
                n = len(visited)
                for v in set(visited) :
                    answer[v]+=n
                    
    return max(answer)
