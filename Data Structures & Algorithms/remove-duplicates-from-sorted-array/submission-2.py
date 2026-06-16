class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=0
        r=0
        while(l<len(nums) and r<len(nums)):
            if nums[l]==nums[r] and r>l:
                nums.pop(r)
            elif nums[l]==nums[r]:
                r+=1
            else:
                r+=1
                l+=1
        return r