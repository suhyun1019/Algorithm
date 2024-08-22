# 시간 복잡도 O(n^3)
#def solution(elements):
#    answer = []
#    n = len(elements)
#    elements = elements+elements
#    for i in range(1, n+1) :
#        for j in range(n) :
#            answer.append(sum(elements[j:j+i]))
#    return len(set(answer))

# 시간 복잡도 O(n^2)
def solution(elements) :
    answer = set()
    n = len(elements)
    elements = elements+elements
    
    for i in range(n) :
        s = 0
        for j in range(n) :
            s+=elements[i+j]
            answer.add(s)
    return len(answer)
