class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res=0
        def dfs(i,currzor):
            nonlocal res
            if i==len(nums):
                return 
            dfs(i+1,currzor)
            res+=(currzor^nums[i])
            dfs(i+1,currzor^nums[i])
        dfs(0,0)
        return res
            