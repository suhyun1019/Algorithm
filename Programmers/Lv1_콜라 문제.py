def solution(a, b, n):
    answer = 0
    take = 1
    while take>0 :
        left = n%a
        take = n//a*b
        answer+= take
        n = take+left
    return answer
