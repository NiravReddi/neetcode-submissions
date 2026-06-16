class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dic=defaultdict(int)
        for i in nums:
            dic[i]+=1
        ind=0
        for i in range(3):
            for j in range(dic[i]):
                nums[ind]=i
                ind+=1
        
        