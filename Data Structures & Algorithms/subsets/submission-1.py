class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(i,s):
            nonlocal res
            
            res.append(list(s))
            if i>=len(nums):
                return
            for k in range(i,len(nums)):

                s.add(nums[k])
                dfs(k+1,s)
                s.remove(nums[k])
        dfs(0,set())
        return res
            
