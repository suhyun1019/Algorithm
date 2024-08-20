# 스택 이용한 올바른 괄호 여부 판단 
def check(s) :
    stack = []
    d = {'(':')', '[':']', '{':'}'}
    
    for e in s :
        if e in d :
            stack.append(e)
        elif stack and d[stack[-1]]==e :
            stack.pop()
        else :
            return False
        
    if stack :
        return False
    else :
        return True

def solution(s):
    answer = 0
    stack = list(s)
    
    for i in range(len(s)) :
        if check(stack) :
            answer+=1
        stack.append(stack.pop(0))
    return answer
