def solution(sticker):
    if len(sticker)<=3:
        return max(sticker)
    
    n = len(sticker)
    dp1 = [0]*n
    dp2 = [0]*n
    
    for i in range(n):
        if i==1:
            dp1[i] = 0
        else:
            dp1[i] = max(dp1[i-2],dp1[i-3])+sticker[i]
    
    for i in range(n):
        if i==0:
            dp2[i] = 0
        else:
            dp2[i] = max(dp2[i-2],dp2[i-3])+sticker[i]
    
    return max(dp1[n-3],dp1[n-2],dp2[n-1],dp2[n-2])
