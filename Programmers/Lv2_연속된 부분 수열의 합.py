# 투포인터, 누적합 
def solution(sequence, k):
    answer = []
    left, right = 0, 0
    s = sequence[left]
    
    while left<=right<len(sequence) :
        if s==k :
            answer.append([left, right])
            s-=sequence[left]
            left+=1
        elif s>k :
            s-=sequence[left]
            left+=1
        else :
            right+=1
            if right<len(sequence) :
                s+=sequence[right]
                
    answer.sort(key=lambda x:(x[1]-x[0], x[0]))
    return answer[0]
