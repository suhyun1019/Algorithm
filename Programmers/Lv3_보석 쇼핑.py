from collections import defaultdict

def solution(gems):
    answer = []
    s = set(gems)
    counter = defaultdict(int)
    left, right = 0, 0
    
    while left<=right<len(gems) :
        counter[gems[right]]+=1
        if len(counter.keys()) == len(s) :
            answer.append([left+1, right+1])
            while left<right<len(gems) and len(counter.keys()) == len(s) :
                counter[gems[left]]-=1
                if counter[gems[left]]==0 :
                    del counter[gems[left]]
                left+=1
            answer.append([left, right+1])
        right+=1
    
    answer.sort(key=lambda x:(x[1]-x[0], x[0]))
    return answer[0]
