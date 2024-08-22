# DFS
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(s, digit, ans) :
            
            num = {1:'', 2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
            if len(digit)==0 :
                ans.append(s)
                return

            for n in num[int(digit[0])] :
                dfs(s+n, digit[1:], ans)
            return 
        
        ans = []
        if len(digits)==0 :
            return ans
        dfs('', list(digits), ans)

        return ans
        
