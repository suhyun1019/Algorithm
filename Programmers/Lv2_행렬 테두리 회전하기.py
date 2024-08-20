def solution(rows, columns, queries):
    answer = []
    l = [[i+j+1 for j in range(columns)] for i in range(0, rows*columns, columns)]
    
    for q in queries :
        x1, y1, x2, y2 = q[0]-1,q[1]-1,q[2]-1,q[3]-1
        last = l[x1][y1]
        m = [l[x1][y1]]
        for i in range(x1, x2) :
            l[i][y1] = l[i+1][y1]
            m.append(l[i+1][y1])
        for i in range(y1, y2) :
            l[x2][i] = l[x2][i+1]
            m.append(l[x2][i+1])
        for i in range(x2, x1, -1) :
            l[i][y2] = l[i-1][y2]
            m.append(l[i-1][y2])
        for i in range(y2, y1+1, -1) :
            l[x1][i] = l[x1][i-1]
            m.append(l[x1][i-1])
        l[x1][y1+1] = last
        answer.append(min(m))
            
    return answer
