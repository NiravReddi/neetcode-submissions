class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dic={}
        res=[]
        for ind,val in enumerate(nums):
            dic[val]=ind
            for i in range(ind+1,len(nums)):
                for j in range(i+1,len(nums)):
                    if -(nums[i]+nums[j]) in dic.keys() and sorted([-(nums[i]+nums[j]),nums[i],nums[j]]) not in res:
                        res.append(sorted([-(nums[i]+nums[j]),nums[i],nums[j]]))
            
        return res
        