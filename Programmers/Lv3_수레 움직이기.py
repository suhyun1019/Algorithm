def solution(maze):
    moves = [(1,0),(0,1),(-1,0),(0,-1)]
    n,m = len(maze), len(maze[0])
    global ans
    ans = 1000
    sr,sb,tr,tb = 0,0,0,0
    
    for i in range(n):
        for j in range(m):
            if maze[i][j]==3:
                tr = [i,j]
            elif maze[i][j]==4:
                tb = [i,j]
            elif maze[i][j]==1:
                sr = [i,j]
            elif maze[i][j]==2:
                sb = [i,j]
    
    def dfs(rx,ry,bx,by,rv,bv,cnt,tr,tb,r,b):
        global ans
        
        #print((rx,ry),(bx,by),rv,bv,cnt)
        if tr == [rx,ry] and tb == [bx,by]: # 도착
            ans = min(ans,cnt)       
        elif tr == [rx,ry]:
            maze[rx][ry] = r
            for mbx,mby in moves:
                dbx,dby = bx+mbx,by+mby
                if 0<=dbx<n and 0<=dby<m and (dbx,dby) not in bv and maze[dbx][dby]!=5 and maze[dbx][dby]!=r:
                    bv.append((dbx,dby))
                    maze[bx][by] = 0
                    maze[dbx][dby] = b
                    dfs(rx,ry,dbx,dby,rv,bv,cnt+1,tr,tb,r,b)
                    bv.pop()
                    maze[bx][by] = b
                    maze[dbx][dby] = 0
        elif tb == [bx,by]:
            maze[bx][by] = b
            for mrx,mry in moves:
                drx,dry = rx+mrx,ry+mry
                if 0<=drx<n and 0<=dry<m and (drx,dry) not in rv and maze[drx][dry]!=5 and maze[drx][dry]!=b:
                    rv.append((drx,dry))
                    maze[rx][ry] = 0
                    maze[drx][dry] = r
                    dfs(drx,dry,bx,by,rv,bv,cnt+1,tr,tb,r,b)
                    rv.pop()
                    maze[rx][ry] = r
                    maze[drx][dry] = 0
        else:
            for mrx,mry in moves:
                drx,dry = rx+mrx,ry+mry
                if 0<=drx<n and 0<=dry<m and (drx,dry) not in rv and maze[drx][dry]!=5 and maze[drx][dry]!=b:
                    rv.append((drx,dry))
                    maze[rx][ry] = 0
                    maze[drx][dry] = r
                    for mbx,mby in moves:
                        dbx,dby = bx+mbx,by+mby
                        if 0<=dbx<n and 0<=dby<m and (dbx,dby) not in bv and maze[dbx][dby]!=5 and maze[dbx][dby]!=r:
                            bv.append((dbx,dby))
                            maze[bx][by] = 0
                            maze[dbx][dby] = b
                            dfs(drx,dry,dbx,dby,rv,bv,cnt+1,tr,tb,r,b)
                            bv.pop()
                            maze[bx][by] = b
                            maze[dbx][dby] = 0
                    rv.pop()
                    maze[rx][ry] = r
                    maze[drx][dry] = 0
        return

    maze_copy = [m[:] for m in maze]
    dfs(sr[0],sr[1],sb[0],sb[1],[(sr[0],sr[1])],[(sb[0],sb[1])],0,tr,tb,1,2)
    maze = [m[:] for m in maze_copy]
    dfs(sb[0],sb[1],sr[0],sr[1],[(sb[0],sb[1])],[(sr[0],sr[1])],0,tb,tr,2,1)
    print(ans)
    return ans if ans!=1000 else 0
