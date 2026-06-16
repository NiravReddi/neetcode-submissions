class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ind=0
        while(ind!=len(nums)):
            if nums[ind]==val:
                nums.remove(val)
            else:
                ind+=1
        return ind
        