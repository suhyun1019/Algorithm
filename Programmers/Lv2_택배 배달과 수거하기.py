# 그리디 
def solution(cap, n, deliveries, pickups):
    answer = 0
    di, pi = n-1, n-1
    if max(deliveries)==0 and max(pickups)==0 :  # 배달과 수거 둘다 안해도 되는 경우 
        return 0
    
    while di>=0 or pi>=0 :
        dc, pc = cap, cap
        answer += max(di+1, pi+1)*2
        while dc>=0 and di>=0 :
            if dc-deliveries[di]<0 :
                deliveries[di]-=dc
                break
            dc-=deliveries[di]
            deliveries[di] = 0
            di-=1
        while pc>=0 and pi>=0 :
            if pc-pickups[pi]<0 :
                pickups[pi]-=pc
                break
            pc-=pickups[pi]
            pickups[pi] = 0
            pi-=1
        
    return answer
