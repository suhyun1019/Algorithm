def solution(k, ranges):
    lc = []
    area = [0]
    res = []
    
    # lc - 우박수 생성 
    while k>1 :
        lc.append(k)
        if k%2==0 :
            k//=2
        else :
            k=k*3+1
    lc.append(1)
    
    # area: 정적분을 위한 누적 넓이 
    t = 0
    for i in range(len(lc)-1) :
        t+=(lc[i]+lc[i+1])/2
        area.append(t)
    
    # res: 정적분 
    n = len(lc)-1
    for r in ranges :
        a,b = r[0], n+r[1]
        if a>b :
            res.append(-1.0)
        else :
            res.append(area[b]-area[a])
            
    return res
