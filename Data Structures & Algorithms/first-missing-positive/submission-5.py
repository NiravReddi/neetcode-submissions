class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        posnums=[False for i in range(1,len(nums)+2)]
        
        for i in nums:
            if i>0 and i<=len(nums):
                posnums[i]=True
        for i in range(1,len(nums)+1):
            if not posnums[i]:
                return i
        return len(nums)+1
        