class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic={}
        for i in nums:
            if i in dic.keys():
                return i
            dic[i]=1