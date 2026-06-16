class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        currsum=0
        res=len(nums)+1
        for r in range(len(nums)):
            currsum+=nums[r]
            while(currsum>=target):
                res=min(res,r-l+1)
                currsum-=nums[l]
                l+=1
        if res==len(nums)+1:
            return 0
        return res