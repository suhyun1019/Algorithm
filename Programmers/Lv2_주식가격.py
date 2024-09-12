def solution(prices):
    stack = []
    answer = [i for i in range(len(prices)-1, -1, -1)]
    t=0
    
    while t<len(prices) :
        if len(stack)==0 or stack[-1][1]<=prices[t] :   # 주식 증가
            stack.append((t, prices[t]))
            t+=1
        else :      # 주식 감소해서 감소한 시점 기록 
            now = stack.pop()
            answer[now[0]] = t-now[0]
            
    return answer
