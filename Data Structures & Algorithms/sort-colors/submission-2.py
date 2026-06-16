class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dic={}
        for ind,val in enumerate(nums):
            if val in dic.keys():
                dic[val].append(ind)
            else:
                dic[val]=[ind]
        ind=0
        for i in [0,1,2]:
            if i in dic.keys():
                for k in range(ind,ind+len(dic[i])):
                    nums[k]=i
                ind+=len(dic[i])
        