def solution(keymap, targets):
    dic = dict()
    for key in keymap :
        for i,k in enumerate(key) :
            if k in dic :
                dic[k] = min(dic[k], i+1)
            else :
                dic[k] = i+1
                
    #print(dic)
    ans = [0]*len(targets)
    for i,target in enumerate(targets) :
        for t in target :
            if t not in dic :
                ans[i]=-1
                break
            else :
                ans[i]+=dic[t]
    
    return ans
