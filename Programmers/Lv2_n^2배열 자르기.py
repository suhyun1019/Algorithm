# 문자열 다루기(슬라이싱) 
def solution(n, left, right):
    res = []
    s1, e1 = left//n, left%n
    s2, e2 = right//n, right%n
    
    for i in range(s1, s2+1) :
        for j in range(n) :
            if j<=i :
                res.append(i+1)
            else :
                res.append(j+1)
    return res[e1:e1+(right-left)+1]
    #return res[e1:max(e2-n+1, len(res)-e1+2)]
