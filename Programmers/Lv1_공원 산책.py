def solution(park, routes):
    dic = {'N':(-1,0), 'S':(1,0), 'W':(0,-1), 'E':(0,1)}
    
    for i in range(len(park)) :
        for j in range(len(park[0])) :
            
            if park[i][j]=='S' :            # 출발!
                for route in routes :       # 모든 명령에 대해 
                    direction, move = route.split()[0], int(route.split()[1])
                    ti, tj = i, j
                    for m in range(move) :  # 방향만큼 이동하면서 조건에 걸리면 해당 명령 무시 
                        i += dic[direction][0]
                        j += dic[direction][1]
                        if i<0 or i>=len(park) or j<0 or j>=len(park[0]) or park[i][j]=='X' :
                            i, j = ti, tj
                            break
                return [i, j]
