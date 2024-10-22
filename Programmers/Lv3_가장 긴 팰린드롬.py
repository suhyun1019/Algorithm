def solution(s):
    answer = 0

    for i in range(len(s)):
        left,right = i,i
        while 0<=left and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        answer = max(answer, right-left-1)
        
        left,right = i,i+1
        while 0<=left and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        answer = max(answer, right-left-1)
        
    return answer
