class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(idx, path) :
            if len(path)==len(digits) :
                ans.append(path)
                return 
            
            for i in range(idx, len(digits)) :  #한자리씩
                for j in dic[digits[i]] :
                    dfs(i+1, path+j)
                    
        
        if not digits :
            return 
        
        dic={"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        ans=[]

        dfs(0, "")
        return ans
