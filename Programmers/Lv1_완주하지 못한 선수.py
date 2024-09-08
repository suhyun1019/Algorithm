from collections import Counter

def solution(participant, completion):
    return (Counter(participant)-Counter(completion)).most_common()[0][0]
