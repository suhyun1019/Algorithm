def solution(string):
    answer = []
    dic = {}
    for i,s in enumerate(string) :
        if s not in dic :   # 같은 글자 없을때
            answer.append(-1)
        else :              # 앞에 같은 글자 있을때
            answer.append(i-dic[s])
        dic[s]=i    # 글자 인덱스 갱신 
    return answer
