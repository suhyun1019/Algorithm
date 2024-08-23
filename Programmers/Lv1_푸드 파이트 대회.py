# 문자열 다루기 
def solution(food):
    answer = ''
    
    for i,f in enumerate(food) :
        if i==0 :
            continue
        answer+=str(i)*(f//2)
        
    return answer+'0'+answer[::-1]
