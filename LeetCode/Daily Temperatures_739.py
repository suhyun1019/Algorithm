#stack 이용한 문제풀기

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans=[0]*len(temperatures)
        s=[]
        
        for i, t in enumerate(temperatures) :
            if len(s)!=0 :
                while temperatures[s[-1]] < t :
                    idx=s.pop()
                    ans[idx]=i-idx
                    if len(s)==0 :
                        break
                
            s.append(i)
            
        return ans
