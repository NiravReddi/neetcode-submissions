class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def prem(ret,i):
            nonlocal res
            
            if ret not in res:
                res.append(ret[:])
            if len(nums)==i:
                return 
            for k in range(i,len(nums)):
                ret.append(nums[k])
                prem(ret,k+1)
                ret.pop()
            return 
        prem([],0)
        return res 