class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic=set()
        i=0
        while(i<len(nums)):
            if nums[i] in dic:
                return nums[i]
            dic.add(nums[i])
            i+=1
        