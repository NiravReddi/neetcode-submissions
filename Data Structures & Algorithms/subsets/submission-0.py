class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]

        def dfs(i,r):
            if i<len(nums):
                res.append(r+[nums[i]])
                dfs(i+1,r+[nums[i]])
                dfs(i+1,r)
        
        dfs(0,[])
        return res

        