class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(num_list) :
            if len(nums)==len(num_list) :
                nlist=num_list[:]
                ans.append(nlist)
                num_list.pop()
                return
            
            for i in nums :
                if i not in num_list :
                    num_list.append(i)
                    dfs(num_list)
            
            if len(num_list)==0 :
                return
            else :
                num_list.pop()
                
        ans=[]
        num_list=[]
        
        dfs(num_list)
        
        return ans
      
      
         """
         파이썬의 itertools 모듈의 permutations 함수 사용해 간단한 풀이
         
         ans=[]
         p= list(itertools.permutations(nums))
         for i in p :
            ans.append(list(i))
         
         return ans
         """
