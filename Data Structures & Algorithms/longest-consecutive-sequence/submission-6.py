class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=1
        if len(nums)==0:
            return 0
        nums=set(nums)
        def seq(curr,ln):
            if curr+1 in nums:
                return seq(curr+1,ln+1)
            else:
                return ln
        for i in nums:
            if i-1 in nums:
                t=seq(i-1,1)
                res=max(t,res)
        return res
        