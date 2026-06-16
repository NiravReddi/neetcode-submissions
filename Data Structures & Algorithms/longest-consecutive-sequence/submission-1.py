class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mx=defaultdict(int)
        res=0
        s=set(nums)
        def consecutive(i):
            if i in s:
                return 1+consecutive(i+1)
            else:
                return 0
        for i in s:
            if i-1 not in s:
                con=consecutive(i)
                res=max(res,con)
        return res
        