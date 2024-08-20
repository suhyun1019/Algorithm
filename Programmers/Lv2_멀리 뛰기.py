import math

def solution(n):
    answer = 0
    i = n
    j = 0
    while j<=n//2 and i>=0:
        answer+=math.comb(i+j, j)
        i-=2
        j+=1
    return answer%1234567
