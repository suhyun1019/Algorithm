import heapq

def solution(operations):
    hq = []
    for oper in operations :
        if oper=="D 1" and hq :
            m = max(hq)
            hq.remove(m)
        elif oper=="D -1" and hq :
            heapq.heappop(hq)
        elif oper.split()[0]=="I" :
            heapq.heappush(hq, int(oper.split()[1]))
        
    return [max(hq), min(hq)] if hq else [0, 0]
