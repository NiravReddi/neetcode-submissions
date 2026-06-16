class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash={}
        for ind,val in enumerate(nums):
            if val in hash.keys():
                return True
            else:
                hash[val]=ind
        return False