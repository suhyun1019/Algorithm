from collections import defaultdict
from itertools import combinations

def solution(friends, gifts):
    dic = {}
    gift_cnt = defaultdict(int)
    
    for friend in friends :
        dic[friend] = defaultdict(int)
    
    for gift in gifts :
        fr, to = gift.split()[0], gift.split()[1]
        dic[fr][to] += 1
        gift_cnt[fr]+=1
        gift_cnt[to]-=1
        
    comb = list(combinations(friends, 2))
    ans = defaultdict(int)
    
    for c in comb :
        a,b = c[0], c[1]
        if b in dic[a] or a in dic[b] :
            if dic[a][b]>dic[b][a] :
                ans[a]+=1
            elif dic[a][b]<dic[b][a] :
                ans[b]+=1
            elif dic[a][b]==dic[b][a] :
                if gift_cnt[a]>gift_cnt[b] :
                    ans[a]+=1
                elif gift_cnt[a]<gift_cnt[b] :
                    ans[b]+=1
        else :
            if gift_cnt[a]>gift_cnt[b] :
                ans[a]+=1
            elif gift_cnt[a]<gift_cnt[b] :
                ans[b]+=1
    
    if ans :
        return sorted(ans.values(), reverse=True)[0]
    else :
        return 0
