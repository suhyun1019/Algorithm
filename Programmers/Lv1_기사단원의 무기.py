import math 

def solution(number, limit, power):
    ans = []
    for i in range(1, number+1) :
        cnt=0
        for j in range(1, int(math.sqrt(i))+1) :    
            if j*j==i : # 제곱근일때
                cnt+=1
            elif i%j==0 :
                cnt+=2
        if cnt>limit :
            cnt = power
        ans.append(cnt)
        
    return sum(ans)
