class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def prem(ret,nums):
            nonlocal res
            if len(nums)==0:
                res.append(ret[:])
                return 
            else:
                for i in range(len(nums)):
                    ret.append(nums.pop(i))
                    prem(ret,nums)
                    nums.insert(i,ret.pop())
                return 
        prem([],nums)
        return res      