class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=list()
        def dfs(i,target,curr):
            if target==0 and curr not in res:
                res.append(curr)
            if target<0 or i>=len(nums):
                return
            
            dfs(i,target-nums[i],curr+[nums[i]])
            dfs(i+1,target,curr)

                    
        dfs(0,target,[])
        return res            