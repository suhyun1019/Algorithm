# 기본적인 진수 변환 
def solution(n):
    su = '412'
    answer = su[n%3]
    while n>3:
        t = n%3
        answer += su[t]
        n = n//3
    
    return answer
