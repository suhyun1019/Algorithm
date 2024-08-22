def solution(cards):
    ans = []
    
    for i in range(1, len(cards)+1) :
        visited = []
        while  i not in visited and cards[i-1]!=0 :
            visited.append(i)
            n = cards[i-1]
            cards[i-1] = 0
            i = n
        
        if visited :
            ans.append(len(visited))
    
    ans.sort()
    if len(ans)<2 :
        return 0
    else :
        return ans[-2]*ans[-1]
