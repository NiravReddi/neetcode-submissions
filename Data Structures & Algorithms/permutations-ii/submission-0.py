class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(nu,ret):
            nonlocal res
            if len(ret)==len(nums):
                if ret not in res:
                    res.append(ret[:])
                return
            for i in range(len(nu)):
                ret.append(nu.pop(i))
                dfs(nu,ret)
                nu.insert(i,ret.pop())
            return
        dfs(nums[:],[])
        return res