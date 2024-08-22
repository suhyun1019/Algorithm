from collections import defaultdict
from collections import Counter

def solution(topping):
    answer = 0
    topping = list(map(str, topping))
    c1, c2 = defaultdict(int), Counter(topping)
    
    for i in range(len(topping)) :
        if len(c1)==len(c2) :
            answer+=1
        c1[topping[i]]+=1
        c2[topping[i]]-=1
        if c2[topping[i]]==0 :
            c2.pop(topping[i])
    return answer
