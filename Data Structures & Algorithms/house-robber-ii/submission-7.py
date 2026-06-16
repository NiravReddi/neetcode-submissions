class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[[-1 for i in range(len(nums))] for k in range(3)]
        if len(nums)==1:
            return nums[0]
        def dfs(i,start):
            if i==len(nums)-1:
                if start==0:
                    dp[start][i]=0
                    return 0
                else:
                    dp[start][i]=nums[i]
                    return nums[i]
            if i>=len(nums):
                return 0
            if dp[start][i]!= -1:
                return dp[start][i]
            dp[start][i]=nums[i]+max(dfs(i+2,start),dfs(i+3,start))
            return dp[start][i]
        
        return max(dfs(0,0),dfs(1,1),dfs(2,2))