class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic={}
        for i in nums:
            if i in dic.keys():
                return True
            dic[i]=i
        return False
        