class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        nums.sort()
        
        def dfs(i,l):
            if l not in res:
                res.append(l)
            if i==len(nums):
                return
            dfs(i+1,l+[nums[i]])
            dfs(i+1,l)

        dfs(0,[])   
            
        
        return res