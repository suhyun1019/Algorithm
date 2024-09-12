def solution(skill, skill_trees):
    answer = 0
    
    for st in skill_trees :
        temp = list(skill)[::-1]
        for s in st :
            if s in temp :
                if s==temp[-1] :
                    temp.pop()
                else :
                    break
            if s==st[-1] :
                answer+=1
        
    return answer
