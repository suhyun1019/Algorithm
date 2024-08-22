class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i, j) :
            
            #방문한 node는 0으로 표시
            grid[i][j]=0
            
            if j<len(grid[0])-1 and grid[i][j+1]=="1" : #동
                dfs(i, j+1) 
            if i<len(grid)-1 and grid[i+1][j] == "1" : #남
                dfs(i+1, j)
            if j>=1 and grid[i][j-1] == "1" : #서
                dfs(i, j-1) 
            if i>=1 and grid[i-1][j] == "1" : #북
                dfs(i-1, j) 
                
                
        cnt=0
        
        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if grid[i][j]=="1" :
                    dfs(i, j)
                    cnt+=1
        return cnt

############################################
# 재풀이 
# DFS

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y) :
            di = [[0,1],[1,0],[-1,0],[0,-1]]
            grid[x][y] = '0'
            for d in di :
                dx, dy = x+d[0], y+d[1]
                if 0<=dx<len(grid) and 0<=dy<len(grid[0]) and grid[dx][dy]=='1' :
                    dfs(dx, dy)
            return
        
        ans = 0
        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if grid[i][j]=='1' :
                    dfs(i, j)
                    ans += 1
        return ans
