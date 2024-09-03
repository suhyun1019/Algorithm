def solution(name, yearning, photos):
    answer = [0]*len(photos)
    dic = {}
    for n,y in zip(name, yearning) :
        dic[n]=y
    
    for i,photo in enumerate(photos) :
        for p in photo :
            if p in dic :
                answer[i]+=dic[p]
                
    return answer
