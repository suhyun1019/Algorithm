import heapq    

def solution(n, works):
    answer = 0
    if sum(works)<=n :
        return 0
    
    hq = []
    for work in works :
        heapq.heappush(hq, -work)
    m1 = heapq.heappop(hq)*(-1)
    
    while n :
        m2 = heapq.heappop(hq)*(-1)
        if n<=m1-m2+1 :
            heapq.heappush(hq, (m1-n)*(-1))
            heapq.heappush(hq, m2*(-1))
            break
        else :
            n -= (m1-m2)+1
            m1 = m2
            heapq.heappush(hq, (m2-1)*(-1))
            
    return sum(h**2 for h in hq)
