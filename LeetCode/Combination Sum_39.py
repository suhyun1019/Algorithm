"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates 
where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(n, nlist) :
            if sum(nlist)==target :         #nlist 합이 target 일때 ans에 복사한 값을 추가하고 nlist의 마지막 원소 삭제
                ans.append(nlist[:])
                nlist.pop()
                return 
            
            for i in candidates :           
                if i>=n and sum(nlist)+i<=target :  #i가 nlist에 추가한 원소보다 큰 값이고 i를 nlist에 추가했을 때 target보다 작거나 같을 때
                    nlist.append(i)
                    dfs(i, nlist)                   #dfs 시작
            
            if len(nlist)!=0 :
                nlist.pop()
                
        candidates.sort()                 #candidates 정렬
        ans=[]
        dfs(candidates[0], [])
        return ans
