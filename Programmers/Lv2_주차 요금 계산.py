from collections import defaultdict
import math

# 딕셔너리 이용해 차들의 누적 시간 계산, 요금 계산 
def solution(fees, records):
    ans = defaultdict(int)
    dic = defaultdict(int)
    baseTime, baseFee, t, f = fees[0], fees[1], fees[2], fees[3]
    
    for record in records :
        rec = record.split()
        time, num, con = rec[0], rec[1], rec[2]
        time = int(time.split(':')[0])*60+int(time.split(':')[1])
        if con == 'IN' :
            dic[num]-=time
        else :
            dic[num]+=time
            
    for k, v in dic.items() :
        if v<=0 :
            v+=23*60+59
        if v<=baseTime :
            ans[k] = baseFee
        else :
            ans[k] = baseFee+math.ceil((v-baseTime)/t)*f
    ans = sorted(ans.items(), key=lambda x:x[0])
    return [v for k,v in ans]
