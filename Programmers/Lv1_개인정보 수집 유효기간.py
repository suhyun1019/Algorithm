# 문자열 다루기
def solution(today, terms, privacies):
    answer = []
    t = today.split('.')
    today = int(t[2])+(int(t[1])-1)*28+(int(t[0])-1)*28*12
    dic = {}
    
    for term in terms :
        dic[term.split()[0]] = int(term.split()[1])
    
    for i, privacy in enumerate(privacies) :
        t, term = privacy[:-2].split('.'), privacy.split()[1]
        day = int(t[2])+(int(t[1])-1)*28+(int(t[0])-1)*28*12 + dic[term]*28-1
        if day<today :
            answer.append(i+1)
        
    return answer
