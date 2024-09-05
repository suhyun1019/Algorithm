def solution(bandage, health, attacks):
    now, pre = 0, 0
    h = health
    
    for attack in attacks :
        now = attack[0]-pre-1   # 연속 성공 시간 
        h += now*bandage[1] + bandage[2]*(now//bandage[0])  # 성공시간만큼+추가 회복량
        h = min(h, health)      # 최대 체력일때 
        h -= attack[1]
        if h<=0 :
            return -1
        pre = attack[0]
        
    return h
