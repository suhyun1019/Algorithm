from collections import Counter
from collections import defaultdict

# 카운터
def solution(want, number, discount):
    answer = 0
    c = defaultdict(int)
    for i in range(len(want)) :
        c[want[i]]=number[i]
        
    for i,d in enumerate(discount) :
        if d in want :
            c1 = Counter(discount[i:i+10])
            if c == c1 :
                answer+=1
    return answer
