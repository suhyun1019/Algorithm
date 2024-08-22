# 3포인터 사용 
def solution(number):
    answer = 0
    number.sort()
    
    for i in range(len(number)-2) :
        left, right = i+1, len(number)-1
        
        while right>=i+2 :
            s = number[i]+number[right]
            while left<right :
                if s+number[left]==0 :
                    answer+=1
                left+=1
            right-=1
            left = i+1
        
    return answer

# 조합 사용 
from itertools import combinations

def solution(number) :
    return list(map(sum, combinations(number, 3))).count(0)
