class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        runsum=0
        l=0
        res=len(nums)+2
        for r in range(len(nums)):
            runsum+=nums[r]
            while(l<=r and runsum>=target):
                res=min(res,r-l+1)
                runsum-=nums[l]
                l+=1
        if res==len(nums)+2:
            return 0  
        return res