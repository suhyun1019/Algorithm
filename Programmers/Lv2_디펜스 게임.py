import heapq

def solution(n, k, enemy):
    answer = 0
    hq = []
    
    for i,e in enumerate(enemy) :
        if n-e>=0 :     # 방어 성공 
            heapq.heappush(hq, (-1)*e)
            n-=e
        else :          # 방어 실패 
            if k>0 :    # 무적권 사용 
                k-=1
                heapq.heappush(hq, (-1)*e)  
                n-=e
                n-=heapq.heappop(hq)
            else :
                return i
                
    return len(enemy)
