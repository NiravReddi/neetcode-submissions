class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=set()
        lastup=0
        for i in range(len(nums)):
            if nums[i] in s:
                continue
            else:
                s.add(nums[i])
                nums[lastup]=nums[i]
                lastup+=1
        return lastup
        