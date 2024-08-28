# 스택 사용
def solution(numbers):
    answer = [-1]*len(numbers)
    stack = []
    
    for i,n in enumerate(numbers) :
        while stack and stack[-1][1]<n :
            p = stack.pop()
            answer[p[0]] = n
        stack.append((i,n))
        
    return answer
