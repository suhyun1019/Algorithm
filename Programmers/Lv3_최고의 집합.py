def solution(n, s):
    answer = []
    if n>s :
        return [-1]
    
    while n :
        d = s//n
        answer.append(d)
        n-=1
        s-=d
    return answer 
