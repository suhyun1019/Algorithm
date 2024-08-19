from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for c in course :
        combi = []
        for order in orders :
            order = sorted(order)
            combi += list(map(''.join, combinations(order, c)))
        counter = Counter(combi).most_common()
        if counter and counter[0][1]>1 :
            m = counter[0][1]
            answer.append([i[0] for i in counter if i[1]==m])
            
    return sorted(sum(answer, []))
