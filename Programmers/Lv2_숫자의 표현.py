def solution(n):
    answer = 0
    s, e = 0, 1
    nlist = [i for i in range(1, n+1)]
    temp = nlist[s]
    
    while s<e and s<len(nlist) and e<=len(nlist) :
        #print(s, e, temp)
        if temp == n :
            answer+=1
            temp -= nlist[s]
            s+=1
        elif temp > n :
            temp -= nlist[s]
            s+=1
        elif temp < n :
            temp += nlist[e]
            e+=1
        
    return answer
