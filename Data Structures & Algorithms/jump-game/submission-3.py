class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res=0
        fuel=nums[0]
        if fuel<=0 and len(nums)>1:
            return False
        for r in range(1,len(nums)):
            
            fuel-=1
            fuel=max(fuel,nums[r])
            if fuel<=0 and r<len(nums)-1:
                return False

          
        return True
        