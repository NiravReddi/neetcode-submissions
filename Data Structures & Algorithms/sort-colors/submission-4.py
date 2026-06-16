class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dic={0:0,1:0,2:0}
        for i in nums:
            dic[i]+=1
        i=0
        while(i<dic[0]):
            nums[i]=0
            i+=1
        while(i<(dic[0])+dic[1]):
            nums[i]=1
            i+=1
        while(i<(dic[0]+dic[1] + dic[2])):
            nums[i]=2
            i+=1
        