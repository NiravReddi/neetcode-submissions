class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic={}
        mx=0
        
        for ind,val in enumerate(nums):
            dic[val]=ind
        def calseq(i):
            if i+1 not in dic.keys():
                return 1
            else:
                return 1 + calseq(i+1)
        for i in dic.keys():
            if i-1 not in dic.keys():
                ret=calseq(i)
                mx=max(mx,ret)
        return mx
        