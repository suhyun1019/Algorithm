def solution(string):
    answer = 0
    temp = [0,0]    # 시작 문자 개수, 나머지 문자 개수 
    start = ''      # 시작 문자
    for i, s in enumerate(string) :
        if start=='' or start == s :    # 시작 문자와 동일할때
            start = s
            temp[0]+=1
        else :                          # 시작 문자와 다를때
            temp[1]+=1
            
        if temp[0]==temp[1] :           # 개수가 같을때 
            answer+=1
            temp = [0,0]
            if i<len(string)-1 :
                start = string[i+1]
    if temp[0]!=temp[1] :
        answer+=1
    return answer
