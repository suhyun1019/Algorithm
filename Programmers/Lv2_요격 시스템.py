def solution(targets):
    answer = 0
    targets.sort(key=lambda x:(x[0], x[1]))
    end = targets[0][1]
    
    for target in targets :
        if target[0]<end :  # 범위 안에 있을때 end 갱신
            end = min(end, target[1])
        else :              # 해당 범위에 없을때
            answer+=1
            end = target[1]
        
    return answer+1
