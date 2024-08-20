import math

def solution(n):
    answer = 2
    if n<=2 :
        return 1
    for i in range(2, n+1) :
        sqrt = int(math.sqrt(i))
        
        for j in range(2, sqrt+1) :
            if i%j==0 :
                break
            if j==sqrt :
                answer+=1

    return answer
