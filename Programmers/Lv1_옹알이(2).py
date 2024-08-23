# 문자열 다루기
def solution(babbling):
    answer = 0
    dic = {'aya':0, 'ye':1, 'woo':2, 'ma':3}
    
    for bab in babbling :
        for k,v in dic.items() :
            if k in bab :
                bab = bab.replace(k, str(dic[k]))
        
        for i in range(len(bab)) :
            if i<len(bab)-1 and bab[i]==bab[i+1] :
                break
            elif bab[i].isalpha() :
                break
            elif i==len(bab)-1 :
                answer+=1
    return answer
