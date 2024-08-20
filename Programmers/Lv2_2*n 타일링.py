import sys
sys.setrecursionlimit(80000)

def solution(n):
    table = [0]*(n+1)
    def dp(k) :
        if k==1 :
            return 1
        elif k==2 :
            return 2
        
        if table[k]==0 :
            table[k]=(dp(k-1)+dp(k-2))%1000000007
        
        return table[k]
    
    answer=dp(n)
    print(answer)
    return answer%1000000007
