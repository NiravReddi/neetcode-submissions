class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        su=0
        l=0
        res=len(nums)+1
        su=nums[l]
        if su>=target:
            res=min(res,1)
            
        for r in range(1,len(nums)):
            su+=nums[r]
            while(su>=target):
                if su>=target:
                    res=min(res,r-l+1)
                su-=nums[l]
                l+=1
                
            
            
        if res==len(nums)+1:
            return 0
        return res