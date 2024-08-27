from itertools import product

# 완전탐색
def solution(users, emoticons):
    answer = []
    emos = []
    prod = list(product([10,20,30,40], repeat=len(emoticons)))
    
    for pro in prod :
        t = [0, 0]      # 서비스 가입수, 매출액 
        for user in users :
            s = 0       # 사용자마다 이모티콘 구매비용 
            for i in range(len(pro)) :
                if pro[i]>=user[0] :
                    s+=emoticons[i]-int(emoticons[i]*pro[i]*0.01)  
                    
            if s>=user[1] : # 이모티콘 구매 비용이 일정가격 이상이면 
                t[0]+=1
            else :
                t[1]+=s
        answer.append(t)
        
    answer.sort(key=lambda x:(-x[0], -x[1]))
    return answer[0]
