"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(n, nlist) :
            ans.append(nlist[:])
            
            if len(nlist)==len(nums) :
                nlist.pop()
                return 
            
            for i in nums :
                if i>n :
                    nlist.append(i)
                    dfs(i, nlist)
            
            if len(nlist)!=0 :
                nlist.pop()
                
        """
        def dfs(idx, path) :
            ans.append(path)
    
            for i in range(idx, len(nums)) :
              dfs(i+1, path+[nums[i]])
        """
                
        ans=[]
        dfs(min(nums)-1, [])
        
        return ans
