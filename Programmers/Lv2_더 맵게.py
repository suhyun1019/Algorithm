import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville :
        m1 = heapq.heappop(scoville)
        if m1<K and len(scoville)==0 :
            return -1
        elif m1>=K :
            return answer
        else :
            m2 = heapq.heappop(scoville)
            heapq.heappush(scoville, m1+m2*2)
        answer+=1
    return answer
