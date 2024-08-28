from collections import Counter
from collections import defaultdict
import math

# 완전탐색
def solution(weights):
    answer = 0
    dic = defaultdict(int)
    counter = Counter(weights)
    s = set(weights)
    weights.sort()
    
    # 짝꿍이 되는 경우 세기
    for i in range(len(weights)) :
        a,b,c = weights[i]*3/2, weights[i]*4/2, weights[i]*4/3
        if a in s :
            dic[a]+=1
        if b in s :
            dic[b]+=1
        if c in s :
            dic[c]+=1
    
    for k,v in counter.items() :
        if v>1:     # 무게가 같은 중복 짝꿍 처리 
            answer+=math.comb(v,2)
        answer+=v*dic[k]  
        
    return answer
