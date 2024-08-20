def solution(s):
    answer = ''
    flag = True
    
    for word in s.split(' ') :
        for i,w in enumerate(word) :
            if i%2 :
                answer+=w.lower()
            else :
                answer+=w.upper()
        answer+=' '
    return answer[:-1]
