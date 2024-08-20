import heapq

def solution1(land):
    dp = [[land[0][i] for i in range(4)] for _ in range(len(land))]
    
    for i in range(1, len(land)) :
        hq = []
        for j in range(4) :
            heapq.heappush(hq, (-dp[i-1][j], j))
        m1, m2 = heapq.heappop(hq), heapq.heappop(hq)
        for j in range(4) :
            if m1[1]!=j :
                dp[i][j] = land[i][j] - m1[0]
            else :
                dp[i][j] = land[i][j] - m2[0]
            
    return max(dp[-1])

def solution(land) :
    dp = [[land[0][i] for i in range(4)] for _ in range(len(land))]

    for i in range(1, len(land)) :
        for j in range(4) :
            dp[i][j] = max(dp[i-1][:j]+dp[i-1][j+1:])+land[i][j]
    
    return max(dp[-1])
