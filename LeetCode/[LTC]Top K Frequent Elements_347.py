class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        counter=collections.Counter(nums)
        most=counter.most_common(k)
        
        for i in most :
            ans.append(i[0])
        
        return ans
