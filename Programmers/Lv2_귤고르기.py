from collections import Counter

def solution(k, tangerine):
    ans, cnt = 0, 0
    counter = Counter(tangerine).most_common()
    for i in range(len(counter)) :
        ans+=counter[i][1]
        if ans>=k :
            return i+1
    return cnt
