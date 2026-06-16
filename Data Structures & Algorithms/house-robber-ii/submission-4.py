class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3:
            mx=0
            for i in nums:
                mx=max(mx,i)
            return mx
        dic={}
        def dfs(i,k):
            if i==len(nums)-1:
                if k==0:
                    return 0
                else:
                    return nums[i]
            if i==len(nums)-2:
                return nums[i]
            if i==(len(nums)-3):
                if k==0:
                    return nums[i]
                else:
                    return nums[i]+nums[i+2]
            if (i,k) in dic.keys():
                return nums[i]+dic[(i,k)]
            else:
                dic[(i,k)]=max(dfs(i+2,k),dfs(i+3,k))
            return nums[i]+dic[(i,k)]
        return max(dfs(0,0),dfs(1,1),dfs(2,2))
                
        