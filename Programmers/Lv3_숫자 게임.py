def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    while B  :
        a, b = A.pop(), B.pop()
        if a<b :
            answer+=1
        else :
            while B :
                b = B.pop()
                if a<b :
                    answer+=1
                    break
            
    return answer
