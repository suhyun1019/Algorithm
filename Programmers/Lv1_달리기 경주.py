def solution(players, callings):
    dic = {} 
    for i,player in enumerate(players) :
        dic[player]=i
    
    for calling in callings :
        i = dic[calling]
        players[i], players[i-1] = players[i-1], players[i]
        dic[players[i-1]]-=1    # 등수 증가
        dic[players[i]]+=1      # 등수 감소
        
    return players
