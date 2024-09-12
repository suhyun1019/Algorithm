def solution(dirs):
    answer = 0
    dic = {"U":(0,1), "D":(0,-1), "R":(1,0), "L":(-1,0)} # UDRL
    rev = {"U":"D", "D":"U", "R":"L", "L":"R"}
    visited = []
    now = (0,0)
    
    for di in dirs :
        x, y = now[0], now[1]
        dx, dy = dic[di][0], dic[di][1] 
        if x+dx>5 or x+dx<-5 or y+dy>5 or y+dy<-5 :
            continue
        if (x, y, di) not in visited :
            answer+=1
            visited.append((x, y, di))
            visited.append((x+dx, y+dy, rev[di]))
        now = (x+dx, y+dy)
    
    return answer
