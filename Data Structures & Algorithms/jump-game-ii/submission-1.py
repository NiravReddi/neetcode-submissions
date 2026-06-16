class Solution:
    def jump(self, nums: List[int]) -> int:
        dp=[-1 for i in range(len(nums))]
        def dfs(i,j):
            if i>len(nums)-1:
                return
            if i==len(nums)-1:
                if dp[i]!=-1:
                    dp[i]=min(dp[i],j)
                else:
                    dp[i]=j
            if dp[i]!= -1:
                return dp[i]
            dp[i]=j
            for k in range(nums[i],0,-1):
                dfs(i+k,j+1)
        dfs(0,0)
        
        return dp[-1]
