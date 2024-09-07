def solution(scores):
    ho = scores[0]
    scores.sort(key=lambda x:(-x[0], x[1]))
    ans, m = [], 0
    
    for score in scores :
        if score[1]>=m :
            m = score[1]
            ans.append(score)
            
    if ho in ans :
        ans.sort(key=lambda x:-sum(x))
        return ans.index(ho)+1
    else :
        return -1
