from collections import defaultdict

# 딕셔너리 이용 
def solution(id_list, report, k):
    dic = defaultdict(set)
    ans = {}
    
    # id_list 순서 유지하기 위해 미리 선언 
    for i in id_list :
        ans[i]=0
        
    for r in report :
        fro,to = r.split()[0],r.split()[1]
        dic[to].add(fro)
    
    for key,val in dic.items() :
        if len(val)>=k :
            for v in val :
                ans[v]+=1
        
    return list(ans.values())
