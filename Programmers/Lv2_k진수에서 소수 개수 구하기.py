import math

# 진수 변환, 소수 판별
def change(n, k) :
    s = ''
    while n :
        s+=str(n%k)
        n//=k
    return s[::-1]

def check(n) :
    if n<2 :
        return False
    
    for i in range(2, int(math.sqrt(n))+1) :
        if n%i==0 :
            return False
    return True
    
def solution(n, k):
    answer=0
    
    slist = change(n,k).split('0')
    for s in slist :
        if s and check(int(s)) :
            answer+=1
    return answer
