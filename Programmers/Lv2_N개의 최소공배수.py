from collections import Counter

def solution(arr):
    answer = Counter()
    
    def cal(n):
        ans = []
        
        while n:
            if n<=3:
                ans.append(n)
                break
            for i in range(2, n+1):
                if n%i==0:
                    ans.append(i)
                    break
            n = n//i
        return Counter(ans)
    
    for a in arr:
        answer = answer|cal(a)
    res = 1
    for k,v in answer.items():
        res*=k**v
    return res
