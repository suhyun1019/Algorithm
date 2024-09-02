# 투포인터
def solution(n, m, section):
    answer = 0
    left, right = 0, 1
    while left<right and left<len(section):
        while right<len(section) and section[right]<section[left]+m :
            right+=1
        left=right
        right+=1
        answer+=1
        
    return answer
