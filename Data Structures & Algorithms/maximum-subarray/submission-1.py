class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx=-1001
        l=0
        sm=0
        for r in range(len(nums)):
            sm+=nums[r]
            mx=max(mx,sm)
            if sm<0:
                sm=0
        return mx