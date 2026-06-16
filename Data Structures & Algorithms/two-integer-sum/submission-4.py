class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for ind,i in enumerate(nums):
            if target-i in dic.keys():
                return [dic[target-i],ind]
            dic[i]=ind
        