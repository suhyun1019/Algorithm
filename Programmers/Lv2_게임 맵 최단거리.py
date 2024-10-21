# BFS
from collections import deque

def solution(maps):
    
    moves = [(1,0),(0,1),(-1,0),(0,-1)]
    n,m = len(maps),len(maps[0])
    visited = [[1]*m for _ in range(n)]
    
    q = deque([(0,0,1)])
    visited[0][0]=0
    
    while q:
        x,y,d = q.popleft()
        if [x,y]==[n-1,m-1]:
            return d
        for mx,my in moves:
            dx,dy = x+mx,y+my
            if 0<=dx<n and 0<=dy<m and visited[dx][dy] and maps[dx][dy]:
                visited[dx][dy] = 0
                q.append((dx,dy,d+1))
    
    return -1
