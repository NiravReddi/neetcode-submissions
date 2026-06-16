class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di={}
        for i in range(len(nums)):
            if nums[i] in di.keys():
                di[nums[i]].append(i)
            else:
                di[nums[i]]=[i]
            if target-nums[i] in di.keys() and i!=di[target-nums[i]][0]:
                return [di[target-nums[i]][0],i]
        for i in range(len(nums)):
            if target-nums[i] in di.keys() and i!=di[target-nums[i]][0]:
                return [di[target-nums[i]][0],i]
        