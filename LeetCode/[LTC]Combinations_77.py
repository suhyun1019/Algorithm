class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums=list(i+1 for i in range(n))
        
        return list(map(list, itertools.combinations(nums, k)))
