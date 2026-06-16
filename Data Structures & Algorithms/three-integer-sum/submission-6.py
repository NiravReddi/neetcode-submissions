class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        dic={}
        for ind,val in enumerate(nums):
            target=val
            for i in range(ind+1,len(nums)):
                if -(target+nums[i]) in dic.keys():
                    for j in dic[-(target+nums[i])]:
                        if j!=ind and j!=i and sorted([nums[i],nums[ind],nums[j]]) not in res:
                            res.append(sorted([nums[i],nums[ind],nums[j]]))
            if val in dic.keys():
                dic[val].append(ind)
            else:
                dic[val]=[ind]
        return res
                    