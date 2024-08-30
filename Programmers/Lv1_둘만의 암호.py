# 문자열 다루기
def solution(string, skip, index):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for s in skip :
        alpha = alpha.replace(str(s), '')
        
    answer = ''
    for s in string :
        i = (alpha.index(s)+index)%(26-len(skip))
        answer+=alpha[i]
    return answer
