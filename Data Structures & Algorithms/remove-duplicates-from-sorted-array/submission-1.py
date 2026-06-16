class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        lastup=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            else:
                nums[lastup]=nums[i]
                lastup+=1
        return lastup
        