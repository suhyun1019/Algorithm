import sys
sys.setrecursionlimit(10000)

# dfs (재귀)
def dfs(x, y, s, maps) :
    
    dire = [[1,0],[0,1],[-1,0],[0,-1]]
    s+= int(maps[x][y])
    maps[x][y] = 'X'
    
    for d in dire :
        dx, dy = x+d[0], y+d[1]
        if 0<=dx<len(maps) and 0<=dy<len(maps[0]) and maps[dx][dy]!='X' :
            s = dfs(dx, dy, s, maps)

    return s

def solution(maps):
    answer = []
    maps = [[maps[i][j] for j in range(len(maps[0]))] for i in range(len(maps))]
    
    for i in range(len(maps)) :
        for j in range(len(maps[0])) :
            if maps[i][j]!='X' :
                answer.append(dfs(i, j, 0, maps))
    answer.sort()
    return answer if answer else [-1]
