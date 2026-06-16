class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last=len(nums)-1
        first=0
        if nums.count(val)==len(nums):
            nums=[]
            return 0
        while(first<=last and first<len(nums)):
            if nums[first]==val:
                while(last > first and nums[last]==val):
                    last-=1
                nums[first],nums[last]=nums[last],nums[first]
                last-=1
            else:
                first+=1
        
        return first
        